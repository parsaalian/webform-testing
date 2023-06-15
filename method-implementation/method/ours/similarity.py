import numpy as np
from openai.embeddings_utils import cosine_similarity


def get_text_similarity(node1, node2):
    embedding1 = node1.features
    embedding2 = node2.features
    try:
        sim = cosine_similarity(embedding1, embedding2)
        return 0 if np.isnan(sim) else sim
    except:
        return 0


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


def get_combined_similarity(model, node1, node2, alpha=0.5):
    text_sim = get_text_similarity(node1, node2)
    structure_sim = get_structure_similarity(model, node1.xpath, node2.xpath)
    if text_sim == 0:
        return structure_sim
    return alpha * text_sim + (1 - alpha) * structure_sim