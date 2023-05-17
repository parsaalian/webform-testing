from selenium.webdriver.common.by import By

from minijax.config import Config
from minijax.crawler import get_driver_container

from minijax.form.parser import parse_form_inputs_without_labels
from minijax.models.value_generator import gpt3_form_handler, chatgpt_form_handler, rule_based_form_handler

from minijax.crawler.action.base import ActionBase


cfg = Config()


class FormAction(ActionBase):
    def __init__(self, xpath, parent_state):
        super().__init__(
            xpath,
            parent_state,
            execution_count=cfg.crawler_config['action']['form']['execution_count']
        )
    
    
    def execute(self):
        driver = get_driver_container().get_driver()
        # find form step
        form = driver.find_element(By.XPATH, self.xpath)
        # fill/fill+parse step
        values = fill_form_conditional(form)
        self.action_data = values
        # submit step
        result = submit_form(form)
        # TODO: add feedback steps
    
    
    def id(self):
        return f'{self.xpath} {str(self.execution_result)}'


def parse_form(form):
    parsed = parse_form_inputs_without_labels(form)

    # TODO: change based on different parsing modes
    # if cfg.model_config['workflow'].form_parser_mode == FormParserMode.BASIC:
    #     return parse_form_inputs_without_labels(form)
    # return parse_form_inputs_without_labels(form)

    return parsed


def fill_form_conditional(form):
    if cfg.model_config['workflow']['filler'] == 'FIXED' or cfg.model_config['workflow']['filler'] == 'RANDOM':
        parsed = parse_form(form)
        return fill_form_basic(form, parsed)
    else:
        return fill_form_llm(form)


def fill_form_basic(form, parsed):
    if cfg.model_config['workflow']['filler'] == 'FIXED':
        return rule_based_form_handler(form, parsed, False)
    else:
        return rule_based_form_handler(form, parsed, True)


def fill_form_llm(form):
    parsed = form
    if cfg.model_config['workflow']['parser'] != 'NONE':
        parsed = parse_form(form)
    
    if cfg.model_config['workflow']['filler'] == 'GPT3-ZERO-SHOT':
        return gpt3_form_handler(parsed, True)
    if cfg.model_config['workflow']['filler'] == 'GPT3-EXAMPLED':
        return gpt3_form_handler(parsed, False)
    if cfg.model_config['workflow']['filler'] == 'GPT3.5':
        return chatgpt_form_handler(parsed, True)
    if cfg.model_config['workflow']['filler'] == 'GPT4':
        return chatgpt_form_handler(parsed, True)
    return None


def submit_form(form):
    submit_button = form.find_element(
        By.XPATH,
        '//button[@type = "submit"] | //input[@type = "submit"]'
    )
    submit_button.click()
    return True