from enum import Enum
from math import floor

from tqdm import tqdm

import spacy
from openai.embeddings_utils import get_embedding as get_embedding_openai


class EdgeDir(Enum):
    IN = 'IN'
    OUT = 'OUT'


class EdgeType(Enum):
    # connection via for attribute
    FOR = 'FOR'
    
    # neighbor connections
    CHILD = 'CHILD'
    # TODO: if no use, change all neighbour types to simple 'NEIGHBOUR'
    NLEFT = 'NLEFT'
    NRIGHT = 'NRIGHT'
    NTOP = 'NTOP'
    NBOTTOM = 'NBOTTOM'


class RelationGraph:
    def __init__(self):
        self._nodes = {}
        self._edges = {}
    
    
    def nodes(self):
        return list(self._nodes.values())
    
    
    def get_node(self, node_id):
        return self._nodes[node_id]
    
    
    def edges(self):
        return list(self._edges.values())
    
    
    def add_node(self, node):
        self._nodes[node.get_id()] = node
    
    
    def remove_node(self, node):
        self._nodes.pop(node.get_id())
    
    
    def add_edge(self, edge):
        source = edge.source
        
        source.add_edge(edge, EdgeDir.OUT)
        
        self._edges[edge.get_id()] = edge
    
    
    def remove_edge(self, edge):
        source = edge.source
        
        source.remove_edge(edge, EdgeDir.OUT)
        
        self._edges.pop(edge.get_id())
    
    
    def get_node_features(self):
        return {
            key: node.get_features() for key, node in self._nodes.items()
        }


def get_input_visible_text(element):
    text = ''
    attrs = element.attrs

    if 'placeholder' in attrs:
        text += f"{attrs['placeholder']} "
    if 'value' in attrs and attrs['value'].strip() != '':
        text += f", value is {attrs['value']} "
    if 'alt' in attrs:
        text += f", alt is {attrs['alt']} "
    
    text = text.strip().strip(', ')
    return text


def get_visible_text(element):
    if element.name == 'input' or \
        element.name == 'select' or \
        element.name == 'textarea':
        return get_input_visible_text(element)
    
    if element.string == None:
        return ''
    
    return str(element.string)


def get_null_embedding(dim=12288):
    return [0 for i in range(dim)]


def get_text_embedding(text, text_embedding_method='ADA', dim=12288):
    if text.strip() == '':
        return get_null_embedding(dim)
    
    if text_embedding_method == 'WORD2VEC':
        # TODO: average/something word2vec embeddings for each word
        pass
    elif text_embedding_method == 'SPACY':
        # https://spacy.io/usage/linguistic-features#vectors-similarity
        nlp = spacy.load("en_core_web_lg")
        doc = nlp(text)
        return doc.vector
    return get_embedding_openai(text.lower())


class RelationNode:
    def __init__(self, element, text_embedding_method='ADA'):
        self.element = element
        
        self.xpath = self._find_xpath(element)
        self.x_span = self._find_span(element, 'x')
        self.y_span = self._find_span(element, 'y')
        
        self.visible_text = self._find_visible_text(element)
        self.features = self._calculate_features(self.visible_text, text_embedding_method)
        
        self.edges = {
            EdgeDir.OUT: {},
        }
        
        self.children_count = 0
    
    
    def _find_xpath(self, element):
        return element.attrs['xpath']
    
    
    def _find_span(self, element, axis):
        return (
            floor(float(element.attrs[f'{axis}_start'])),
            floor(float(element.attrs[f'{axis}_end']))
        )
    
    
    def _find_visible_text(self, element):
        return get_visible_text(element)
    
    
    def _calculate_features(self, visible_text, text_embedding_method='ADA'):
        features = get_text_embedding(visible_text, text_embedding_method)
        return features
    
    
    def _change_children_count(self, edge, direction, increase=1):
        if edge.type == EdgeType.CHILD and direction == EdgeDir.OUT:
            self.children_count += increase
    
    
    def has_children(self):
        return self.children_count > 0
    
    
    def get_children(self):
        return list(filter(
            lambda x: x.type == EdgeType.CHILD,
            list(self.edges[EdgeDir.OUT].values())
        ))
    
    
    def add_edge(self, edge, direction):
        self.edges[direction][edge.get_id()] = edge
        self._change_children_count(edge, direction, 1)
    
    
    def remove_edge(self, edge, direction):
        self.edges[direction].pop(edge.get_id())
        self._change_children_count(edge, direction, -1)
    
    
    def get_visible_area(self):
        return (self.x_span[1] - self.x_span[0]) * (self.y_span[1] - self.y_span[0])
    
    
    def get_id(self):
        if 'id' in self.element.attrs:
            return self.element.attrs['id']
        return self.xpath
    
    
    def __repr__(self):
        return str(self)


    def __str__(self):
        return f'<{self.element.name}>{self.visible_text}</{self.element.name}> at y: {str(self.y_span)}, x: {str(self.x_span)}'


class RelationEdge:
    def __init__(self, source, target, conn_type):
        self.source = source
        self.target = target
        self.type = conn_type
        self.weight = 0
    
    
    def set_weight(self, weight):
        self.weight = weight
    
    
    def get_id(self):
        return f'edge {self.type.value} from {self.source} to {self.target}'
    
    
    def __repr__(self):
        return str(self)
    
    
    def __str__(self):
        return f'edge {self.type.value} weight {self.weight} from {self.source} to {self.target}'


def create_relations_graph(bs_doc, text_embedding_method='ADA'):
    graph = RelationGraph()
    
    for n in tqdm(bs_doc):
        node = RelationNode(n, text_embedding_method)
        graph.add_node(node)

    return graph
