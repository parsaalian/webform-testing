from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from minijax.logger import logger
from minijax.utils.functional import get_or_else


def parse_generated_commands(commands_text):
    values = {}
    commands = commands_text.strip('\n').split('\n')
    for command in commands:
        cmd, xpath, value = command.split('----')
        value = value.strip('"')
        values[xpath] = (cmd, value)
    return values


def execute_generated_commands(form, commands):
    filled_values = {}
    for xpath, (cmd, value) in commands.items():
        logger.debug(f'{cmd}, {xpath}, {value}')
        if cmd == 'FILL':
            form.find_element(By.XPATH, xpath).send_keys(value)
        elif cmd == 'SELECT':
            select = Select(form.find_element(By.XPATH, xpath))
            select.select_by_visible_text(value)
        elif cmd == 'CLICK':
            form.find_element(By.XPATH, xpath).click()
        filled_values[xpath] = value
    return filled_values


def generate_commands_from_values(form, values):
    command_values = {}
    for xpath, value in values.items():
        element = form.find_element(By.XPATH, xpath)
        tag_name = element.tag_name
        input_type = get_or_else(element.attributes, 'type', 'text')
        if tag_name == 'select':
            command_values[xpath] = ('SELECT', value)
        elif tag_name == 'input' and (input_type == 'checkbox' or input_type == 'radio'):
            command_values[xpath] = ('CLICK', value)
        else:
            command_values[xpath] = ('FILL', value)
    return command_values
