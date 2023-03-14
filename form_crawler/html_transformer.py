import re
from scipy.spatial import KDTree
from webcolors import CSS3_HEX_TO_NAMES, hex_to_rgb
from bs4 import BeautifulSoup as bs, NavigableString, Comment
from selenium.webdriver.common.by import By


IMPORTANT_PROPERTIES = ['backgroundColor', 'color', 'borderColor', 'fontSize', 'fontWeight']
FONT_WEIGHT_NAMES = {
        '100': 'thin',
        '200': 'extra light',
        '300': 'light',
        '400': 'normal',
        '500': 'medium',
        '600': 'semi bold',
        '700': 'bold',
        '800': 'extra bold',
        '900': 'heavy',
}
UNNECESSARY_TAGS = [
    'style', 'script', 'noscript', 'link'
]
INFORMATION_CUTOFF = 0.8
COLOR_KDT_TREE = None
COLOR_NAMES = None


def convert_rgb_to_names(rgb_tuple):
    global COLOR_KDT_TREE, COLOR_NAMES
    
    if COLOR_KDT_TREE is None:
        css3_db = CSS3_HEX_TO_NAMES
        COLOR_NAMES = []
        rgb_values = []
        for color_hex, color_name in css3_db.items():
            COLOR_NAMES.append(color_name)
            rgb_values.append(hex_to_rgb(color_hex))
        
        COLOR_KDT_TREE = KDTree(rgb_values)
    
    _, index = COLOR_KDT_TREE.query(rgb_tuple)
    
    return COLOR_NAMES[index]


def convert_color(rgba_string):
    rgba_tuple = list(
        map(
            lambda x: int(x),
            re.findall(r'\d+', rgba_string)
        )
    )
    alpha = 1 if len(rgba_tuple) == 3 else rgba_tuple[3]
    color_name = convert_rgb_to_names(rgba_tuple[:3])
    return '{0} {1}'.format(color_name, alpha)


def convert_font_weight(font_weight):
    global FONT_WEIGHT_NAMES
    return FONT_WEIGHT_NAMES[font_weight]


def embed_properties_into_element(driver, element):
    global IMPORTANT_PROPERTIES
    
    properties = driver.execute_script('''
        const style = window.getComputedStyle(arguments[0]);
        console.log(style);
        const properties = {};
        Object.keys(style).forEach((key) => {
            if (isNaN(key)) {
                properties[key] = style[key];
            }
        });
        return properties;
    ''', element)
    
    property_converters = {
        'color': convert_color,
        'backgroundColor': convert_color,
        'borderColor': convert_color,
        'fontWeight': convert_font_weight
    }
    
    script_to_execute = ''
    for p in IMPORTANT_PROPERTIES:
        value = properties[p]
        if p in property_converters:
            value = property_converters[p](value)
        script_to_execute += "arguments[0].setAttribute('{0}', '{1}');".format(p, value)
    driver.execute_script(script_to_execute, element)


def merge_attributes(parent_attributes, child_attributes):
    merged = parent_attributes.copy()
    for key, value in child_attributes.items():
        merged[key] = value
    return merged


def merge_single_child_parents(root):
    children = list(root.children)
    if len(children) > 1:
        for child in children:
            merge_single_child_parents(child)
    if len(children) == 1 and type(children[0]) != NavigableString:
        only_child = children[0]
        root.attrs = merge_attributes(root.attrs, only_child.attrs)
        childs_children = list(only_child.children)
        for i in range(len(childs_children)):
            root.insert(i + 1, childs_children[i])
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


def simplify_form(driver, form):
    queue = [form]
    
    while len(queue) > 0:
        element = queue[0]
        size = element.size
        # remove element if it has no size
        if size['height'] == 0 or size['width'] == 0:
            driver.execute_script("return arguments[0].remove();", element);
        # embeds css properties into element
        else:
            children = element.find_elements(By.XPATH, '*')
            queue = [*queue, *children]
            embed_properties_into_element(driver, element)
        queue = queue[1:]
    
    doc = bs(form.get_attribute('innerHTML'), features="html.parser")
    
    for element in doc.find_all():
        if type(element) == Comment or element.name in UNNECESSARY_TAGS:
            element.extract()
        elif type(element) != NavigableString:
            del element['class']
            del element['style']
            # for icons: remove unnecessary data of the icon
            del element['d']
    
    merge_single_child_parents(doc.form)
    
    map_font_sizes(doc)
    
    map_font_weight(doc)
    
    return str(doc)