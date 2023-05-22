import yaml

from bs4 import BeautifulSoup as bs, NavigableString, Comment
from selenium.webdriver.common.by import By

from minijax.crawler.driver import get_driver_container


driver = get_driver_container().get_driver()

process_settings = yaml.load(open('configs/html_process.yaml', 'r'), Loader=yaml.FullLoader)
REDUNDANT_TAGS = process_settings['redundant_tags']
KEEP_ATTRIBUTES = process_settings['keep_attributes']


def embed_element_size_into_element(root):
    queue = [root]
    while len(queue) > 0:
        element = queue[0]
        size = element.size
        
        driver.execute_script("arguments[0].setAttribute('display-width', arguments[1])", element, size['width'])
        driver.execute_script("arguments[0].setAttribute('display-height', arguments[1])", element, size['height'])
        
        children = element.find_elements(By.XPATH, '*')
        queue.extend(children)
        queue.pop(0)
    
    return root


def remove_comments_from_doc(doc):
    comments = doc.findAll(text=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()
    
    return doc


def is_not_processable(tag):
    return isinstance(tag, Comment) or isinstance(tag, NavigableString)


def remove_hidden_tags(doc):
    for tag in doc.findAll(True):
        if is_not_processable(tag):
            continue
        if tag['display-width'] == 0 or tag['display-height'] == 0:
            tag.extract()
    
    return doc


def remove_redundant_tags(doc):
    for tag in doc.findAll(True):
        if is_not_processable(tag):
            continue
        if tag.name in REDUNDANT_TAGS:
            tag.extract()
    
    return doc

def remove_redundant_attributes(doc):
    for tag in doc.findAll(True):
        if is_not_processable(tag):
            continue
        for attr in [a for a in tag.attrs if a not in KEEP_ATTRIBUTES]:
            del tag[attr]
    
    return doc


def tags_have_attribute_conflict(tag1, tag2):
    for attr in tag1.attrs:
        if attr in tag2.attrs and tag1[attr] != tag2[attr]:
            return True
    
    return False


def merge_tags_attributes(tag1, tag2):
    for attr in tag2.attrs:
        if attr not in tag1.attrs:
            tag1[attr] = tag2[attr]
        elif tag1[attr] != tag2[attr]:
            tag1[attr] = tag1[attr] + ' ' + tag2[attr]
    
    return tag1


def conditional_merge_children(root):
    '''
    This function merges children with their parents if they have the following conditions:
    1. They have the same tag name
    2. They don't have attribute conflicts
    3. The parent has only one child
    '''
    children = list(root.children)
    
    if len(children) == 0:
        return root
    
    if len(children) > 1:
        for child in children:
            conditional_merge_children(child)
        return root

    child = children[0]
    
    if is_not_processable(child):
        return root
    
    if tags_have_attribute_conflict(root, child):
        return root

    root = merge_tags_attributes(root, child)
    # append all of child's children to root
    for child_child in child.children:
        root.append(child_child)
    # remove child
    child.extract()
    
    root = conditional_merge_children(root)
    return root


def simplify_element(element):
    # Selenium pre-processing
    element = embed_element_size_into_element(element)

    # process element
    bs_doc = bs(element.get_attribute('outerHTML'), 'html.parser')
    bs_doc = remove_comments_from_doc(bs_doc)
    bs_doc = remove_hidden_tags(bs_doc)
    bs_doc = remove_redundant_tags(bs_doc)
    bs_doc = remove_redundant_attributes(bs_doc)
    bs_doc = conditional_merge_children(bs_doc)
    
    return str(bs_doc)
