import rstr
import random

from selenium.webdriver.support.ui import Select

from minijax.utils.get_or_else import get_or_else
from minijax.crawler.driver import get_driver_container
from minijax.crawler.utils import get_element_xpath

from .utils import parse_generated_commands, execute_generated_commands


driver = get_driver_container().get_driver()


fixed_rules = {
    'text': lambda: 'test',
    'email': lambda: 'test@test.com',
    'password': lambda: 'test',
    'number': lambda: '0',
    'range': lambda: '0',
    'date': lambda: '2020-01-01',
    'time': lambda: '00:00',
    'datetime-local': lambda: '2020-01-01T00:00',
    'week': lambda: '2020-W01',
    'month': lambda: '2020-01',
    'tel': lambda: '0123456789',
    'url': lambda: 'https://test.com',
    'color': lambda: '#000000',
    
    'boolean': lambda: True,
    'select': lambda _: 0,
}


random_rules = {
    'text': lambda: rstr.xeger(r'[A-Za-z0-9]{10}'),
    'email': lambda: rstr.xeger(r'[A-Za-z0-9]{10}') + '@' + rstr.xeger(r'[A-Za-z0-9]{10}') + '.com',
    'password': lambda: rstr.xeger(r'[A-Za-z0-9]{10}'),
    'number': lambda: random.randint(0, 1000),
    'range': lambda: random.randint(0, 1000),
    'date': lambda: rstr.xeger(r'[0-9]{4}') + '-' + rstr.xeger(r'[0-9]{2}') + '-' + rstr.xeger(r'[0-9]{2}'),
    'time': lambda: rstr.xeger(r'[0-9]{2}') + ':' + rstr.xeger(r'[0-9]{2}'),
    'datetime-local': lambda: rstr.xeger(r'[0-9]{4}') + '-' + rstr.xeger(r'[0-9]{2}') + '-' + rstr.xeger(r'[0-9]{2}') + 'T' + rstr.xeger(r'[0-9]{2}') + ':' + rstr.xeger(r'[0-9]{2}'),
    'week': lambda: rstr.xeger(r'[0-9]{4}') + '-W' + rstr.xeger(r'[0-9]{2}'),
    'month': lambda: rstr.xeger(r'[0-9]{4}') + '-' + rstr.xeger(r'[0-9]{2}'),
    'tel': lambda: rstr.xeger(r'[0-9]{10}'),
    'url': lambda: 'https://' + rstr.xeger(r'[A-Za-z0-9]{10}') + '.com',
    'color': lambda: '#' + rstr.xeger(r'[0-9A-Fa-f]{6}'),
    
    'boolean': lambda: True if random.randint(0, 1) == 0 else False,
    'select': lambda element: random.randint(0, len(Select(element).options) - 1),
}


def append_command(commands, cmd, xpath, value):
    commands += f'{cmd}----{xpath}----"{value}"' + '\n'
    return commands


def rule_based_response_generator(parsed_form, random=True):
    rules = random_rules if random else fixed_rules
    commands = ''
    
    for e in parsed_form:
        element = e['element']
        tag = e['tag']
        attributes = e['attributes']
        input_type = get_or_else(attributes, 'type', 'text')
        xpath = get_element_xpath(element)
        
        # skip conditions
        if tag == 'button':
            continue
        elif input_type == 'hidden' or get_or_else(attributes, 'hidden', 'false') == 'true':
            continue
        # tag-based conditions
        elif tag == 'select':
            commands = append_command(commands, 'SELECT', xpath, rules['select'](element))
        # type-based conditions
        elif (
            input_type == 'checkbox' or input_type == 'radio'
        ) and rules['boolean']():
            commands = append_command(commands, 'CLICK', xpath, '')
        else:
            commands = append_command(commands, 'FILL', xpath, rules[input_type]())
    
    return commands


def rule_based_form_handler(form, parsed_form, random=True):
    response = rule_based_response_generator(parsed_form, random=random)
    
    commands = parse_generated_commands(response)
    values = execute_generated_commands(form, commands)
    
    return values