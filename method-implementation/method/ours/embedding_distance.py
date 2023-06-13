import numpy as np
from tqdm import tqdm
from openai.embeddings_utils import cosine_similarity

import networkx as nx
from node2vec import Node2Vec

from bs4 import NavigableString, Comment

from .relation_graph import EdgeDir, EdgeType


def get_text_similarity(node1, node2):
    embedding1 = node1.features
    embedding2 = node2.features
    try:
        sim = cosine_similarity(embedding1, embedding2)
        return 0 if np.isnan(sim) else sim
    except:
        return 0


# Function to create a graph from the BeautifulSoup object
def create_graph(soup):
    G = nx.DiGraph()

    for tag in soup.find_all():
        # Assuming 'xpath' attribute exists for each tag
        xpath = tag.attrs['xpath']
        
        if xpath not in G:
            G.add_node(xpath)
        for child in tag.children:
            if isinstance(child, Comment) or isinstance(child, NavigableString):
                continue
            child_xpath = child.attrs.get('xpath')
            if child_xpath not in G:
                G.add_node(child_xpath)
            G.add_edge(xpath, child_xpath)

    return G


# Function to generate embeddings
def generate_embeddings(G, dimensions=1024, walk_length=30, num_walks=200, workers=4):
    # Create Node2Vec object
    node2vec = Node2Vec(G, dimensions=dimensions, walk_length=walk_length, num_walks=num_walks, workers=workers)

    # Train Node2Vec model
    model = node2vec.fit(window=10, min_count=1, batch_words=4)
    
    return model


def create_node2vec_model(form_doc):
    # Create graph
    G = create_graph(form_doc)

    # Generate embeddings
    model = generate_embeddings(G)
    
    return model


def get_structure_similarity(model, xpath1, xpath2):
    # Check if XPaths exist in the model
    if xpath1 not in model.wv or xpath2 not in model.wv:
        print("One or both of the XPaths are not in the model.")
        return None

    # Get vectors for XPaths
    vector1 = model.wv[xpath1]
    vector2 = model.wv[xpath2]

    # Calculate and return cosine similarity
    return cosine_similarity(vector1, vector2)


def combined_similarity(model, node1, node2, alpha=0.5):
    text_sim = get_text_similarity(node1, node2)
    structure_sim = get_structure_similarity(model, node1.xpath, node2.xpath)
    if text_sim == 0:
        return structure_sim
    return alpha * text_sim + (1 - alpha) * structure_sim


def add_weight_to_graph(model, relation_graph):
    for node in tqdm(relation_graph.nodes()):
        edges = list(node.edges[EdgeDir.OUT].values())
        
        for edge in edges:
            if edge.type == EdgeType.CHILD:
                continue
            sim = combined_similarity(model, edge.source, edge.target)
            if edge.target.has_children():
                for target_child_edge in edge.target.get_children():
                    sim = max(
                        sim,
                        combined_similarity(model, edge.source, target_child_edge.target)
                    )
            edge.set_weight(sim)
    return relation_graph


def cutoff_low_score_edges(relation_graph, factor=1):
    scores = list(filter(
        lambda x: x != 0,
        map(
            lambda x: x.weight,
            relation_graph.edges()
        )
    ))
    
    mean = np.mean(scores)
    std_dev = np.std(scores)

    # Set the cutoff to be one standard deviation above the mean
    cutoff = mean + factor * std_dev

    print("Mean:", mean)
    print("Standard Deviation:", std_dev)
    print("Cutoff:", cutoff)
    
    for edge in relation_graph.edges():
        if edge.type != EdgeType.CHILD and edge.weight < cutoff:
            relation_graph.remove_edge(edge)
    
    return relation_graph