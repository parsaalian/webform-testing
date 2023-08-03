import spacy
from openai.embeddings_utils import get_embedding as get_embedding_openai


def get_null_embedding(dim=12288):
    return [0 for _ in range(dim)]


def get_spacy_embedding(text):
    # https://spacy.io/usage/linguistic-features#vectors-similarity
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    return doc.vector


def get_ada_embedding(text):
    return get_embedding_openai(text.lower())


def get_text_embedding(text, text_embedding_method='ADA', dim=12288):
    if text.strip() == '':
        return get_null_embedding(dim)
    
    if text_embedding_method == 'WORD2VEC':
        # TODO: average/something word2vec embeddings for each word
        pass
    elif text_embedding_method == 'SPACY':
        return get_spacy_embedding(text)
    return get_ada_embedding(text)
