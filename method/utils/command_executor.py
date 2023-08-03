from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def strip_value(value):
    while value[0] == '"' or value[-1] == '"':
        value = value.strip('"')
    
    return value


def parse_single_command(command_text):
    command = command_text.split('----')
    if len(command) == 2 and command[0] != 'CLICK' and command[0] != 'BLANK':
        raise Exception(f'Invalid command: {command_text}')
    if len(command) == 3 and command[0] != 'FILL' and command[0] != 'SELECT':
        raise Exception(f'Invalid command: {command_text}')
    
    cmd, xpath = command[0], command[1]
    value = strip_value(command[2]) if len(command) == 3 else None
    
    return cmd, xpath, value


def parse_generated_commands(commands_text):
    values = {}
    commands = commands_text.strip('\n').split('\n')
    for command in commands:
        cmd, xpath, value = parse_single_command(command)
        values[xpath] = (cmd, value)
    return values


def execute_generated_commands(form, commands):
    filled_values = {}
    for xpath, (cmd, value) in commands.items():
        if cmd == 'FILL':
            form.find_element(By.XPATH, xpath).send_keys(value)
        elif cmd == 'SELECT':
            select = Select(form.find_element(By.XPATH, xpath))
            select.select_by_visible_text(value)
        elif cmd == 'CLICK':
            form.find_element(By.XPATH, xpath).click()
        elif cmd == 'BLANK':
            pass
        filled_values[xpath] = value

    return filled_values


def generate_commands_from_values(form, values):
    command_values = {}
    for xpath, value in values.items():
        element = form.find_element(By.XPATH, xpath)
        tag_name = element.tag_name
        try:
            input_type = element.attributes['type']
        except:
            input_type = 'text'
        
        if tag_name == 'select':
            command_values[xpath] = ('SELECT', value)
        
        elif tag_name == 'input' and (input_type == 'checkbox' or input_type == 'radio'):
            command_values[xpath] = ('CLICK', value)
        
        else:
            command_values[xpath] = ('FILL', value)
    
    return command_values
