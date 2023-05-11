import networkx as nx
from node2vec import Node2Vec
import matplotlib.pyplot as plt
from collections import defaultdict
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://ant.design/components/form#register"
driver.get(URL)

form = driver.find_element(By.ID, 'register')

ex0 = form.get_attribute('outerHTML')
d = soup(ex0, 'html.parser')

def _traverse_html(_d:soup, _graph:nx.Graph, _counter, _parent=None) -> None:
    for i in _d.contents:
        if i.name is not None:
            try:
                _name_count = _counter.get(i.name)
                if _parent is not None:
                    _graph.add_node(_parent)
                    _graph.add_edge(_parent, i.name if not _name_count else f'{i.name}_{_name_count}')
                _counter[i.name] += 1
                _traverse_html(i, _graph, _counter, i.name)
            except AttributeError:
                pass
        

_full_graph = nx.Graph()
_traverse_html(d, _full_graph, defaultdict(int))

EMBEDDING_FILENAME = 'form.embeddings'
EMBEDDING_MODEL_FILENAME = 'form.model'

# Precompute probabilities and generate walks - **ON WINDOWS ONLY WORKS WITH workers=1**
node2vec = Node2Vec(_full_graph, dimensions=64, walk_length=30, num_walks=200, workers=4)  # Use temp_folder for big graphs

# Embed nodes
model = node2vec.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `dimensions` and `workers` are automatically passed (from the Node2Vec constructor)

# Look for most similar nodes
# model.wv.most_similar('2')  # Output node names are always strings

# Save embeddings for later use
model.wv.save_word2vec_format(EMBEDDING_FILENAME)

# Save model for later use
model.save(EMBEDDING_MODEL_FILENAME)