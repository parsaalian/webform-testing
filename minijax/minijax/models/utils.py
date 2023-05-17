from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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
        print(xpath, cmd, value)
        if cmd == 'FILL':
            form.find_element(By.XPATH, xpath).send_keys(value)
        elif cmd == 'SELECT':
            select = Select(form.find_element(By.XPATH, xpath))
            select.select_by_visible_text(value)
        elif cmd == 'CLICK':
            form.find_element(By.XPATH, xpath).click()
        filled_values[xpath] = value
    return filled_values