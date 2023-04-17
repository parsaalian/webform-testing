from bs4 import NavigableString, Comment


UNNECESSARY_TAGS = [
    'style', 'script', 'noscript', 'link'
]


def merge_attributes(parent_attributes, child_attributes):
    merged = parent_attributes.copy()
    for key, value in child_attributes.items():
        merged[key] = value
    return merged


def merge_single_child_parents(root):
    if type(root) == NavigableString or type(root) == Comment:
        return
    children = list(root.children)
    if len(children) > 1:
        for child in children:
            merge_single_child_parents(child)
    elif len(children) == 1 and type(children[0]) != NavigableString:
        only_child = children[0]
        root.attrs = merge_attributes(
            root.attrs,
            only_child.attrs
        )
        children_children = list(only_child.children)
        for i in range(len(children_children)):
            root.insert(i + 1, children_children[i])
        only_child.extract()
        merge_single_child_parents(root)


def find_attribute_count(doc, attribute):
    counter = {}
    for element in doc.find_all():
        attr_value = element.attrs[attribute]
        if attr_value not in counter:
            counter[attr_value] = 0
        counter[attr_value] += 1
    counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    
    max_value = list(counter.values())[0]
    for key in counter.keys():
        counter[key] /= max_value
    return counter


# you can do this with colors as well, but the dark-mode/light-mode can cause problems in understanding
def map_font_sizes(doc):
    font_count = find_attribute_count(doc, 'fontsize')
    max_repeated_font_size = int(list(font_count.keys())[0].replace('px', ''))
    for element in doc.find_all():
        if type(element) != NavigableString:
            element.attrs['fontsize'] = int(element.attrs['fontsize'].replace('px', '')) / max_repeated_font_size
            if 'fontsize' in element.attrs and element.attrs['fontsize'] == 1:
                del element.attrs['fontsize']


def map_font_weight(doc):
    for element in doc.find_all():
        if type(element) != NavigableString:
            if 'fontweight' in element.attrs and element.attrs['fontweight'] == 'normal':
                del element.attrs['fontweight']


def simplify_doc(doc):
    for element in doc.find_all():
        if type(element) == Comment or element.name in UNNECESSARY_TAGS:
            element.extract()
        
        elif type(element) != NavigableString:
            del element['class']
            del element['style']
            # for icons: remove unnecessary data of the icon
            del element['d']
            # remove angular attributes
            angular_attributes = []
            for attr in element.attrs:
                if "_ng" in attr or "router" in attr:
                    angular_attributes.append(attr)
            for attr in angular_attributes:
                del element[attr]
    
    # change it to take names of tags into account
    # merge_single_child_parents(doc)
    
    # these two functions remove the most repeated value for attributes. Can help with uncluttering the page
    # map_font_sizes(doc)
    # map_font_weight(doc)
    
    return doc