from selenium.webdriver.common.by import By

from minijax.config import Config
from minijax.crawler import get_driver_container
from minijax.crawler.utils import get_element_xpath

from minijax.form.finder import find_forms_by_query
from minijax.form.parser import parse_form_inputs_without_labels
from minijax.form.filler import fill_form_with_fixed_values, fill_form_with_random_values
from minijax.form.gpt3_handler import fill_form_gpt3

from minijax.crawler.action.base import ActionBase


cfg = Config()


class FormAction(ActionBase):
    def __init__(self, xpath):
        super().__init__(xpath, execution_count=cfg.crawler_config['action']['form']['execution_count'])
    
    
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


def find_form_actions(driver):
    # TODO: change based on different finding modes
    forms = find_forms_by_query(driver)
    # if cfg.model_config.form_finder_mode == FormFinderMode.BASIC:
    #     forms = find_forms_by_query(driver)
    # else:
    #     forms = find_forms_by_query(driver)
    
    # TODO: write a common function for all different action types
    forms = list(filter(lambda x: x.is_displayed(), forms))
    forms_xpath = list(map(
        lambda x: get_element_xpath(driver, x),
        forms
    ))
    forms_actions = list(map(
        lambda x: FormAction(x),
        forms_xpath
    ))
    return forms_actions


def parse_form(form):
    parsed = parse_form_inputs_without_labels(form)

    # TODO: change based on different parsing modes
    # if cfg.model_config.form_parser_mode == FormParserMode.BASIC:
    #     return parse_form_inputs_without_labels(form)
    # return parse_form_inputs_without_labels(form)

    return parsed


def fill_form_conditional(form):
    if cfg.model_config['filler'] == 'FIXED' or cfg.model_config['filler'] == 'RANDOM':
        parsed = parse_form(form)
        return fill_form_basic(parsed)
    else:
        return fill_form_llm(form)


def fill_form_basic(form):
    if cfg.model_config['filler'] == 'FIXED':
        return fill_form_with_fixed_values(form)
    else:
        return fill_form_with_random_values(form)


def fill_form_llm(form):
    parsed = form
    if cfg.model_config['parser'] != 'NONE':
        parsed = parse_form(form)
    
    if cfg.model_config['filler'] == 'GPT3-ZERO-SHOT':
        return fill_form_gpt3(parsed, True)
    if cfg.model_config['filler'] == 'GPT3-EXAMPLED':
        return fill_form_gpt3(parsed, False)
    return None


def submit_form(form):
    submit_button = form.find_element(
        By.XPATH,
        '//button[@type = "submit"] | //input[@type = "submit"]'
    )
    print(submit_button.get_attribute('outerHTML'))
    submit_button.click()
    return True