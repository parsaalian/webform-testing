import re

from scipy.spatial import KDTree
from webcolors import CSS3_HEX_TO_NAMES, hex_to_rgb

from bs4 import BeautifulSoup as bs
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


def driver_to_doc(driver, html_element, embed_css=False):
    queue = [html_element]
    
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
            if embed_css:
                embed_properties_into_element(driver, element)
        queue = queue[1:]
    
    doc = bs(html_element.get_attribute('outerHTML'), features="html.parser")
    
    return doc
