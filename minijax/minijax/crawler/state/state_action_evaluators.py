from selenium.webdriver.common.by import By

from minijax.crawler import get_driver_container
from minijax.crawler.utils import get_element_xpath
from minijax.crawler.action import (
    FormAction,
    ClickAction,
)
from minijax.models.workflow import Workflow


workflow = Workflow()
driver = get_driver_container().get_driver()


def filter_hidden_elements(elements):
    return list(filter(lambda x: x.is_displayed(), elements))


def map_elements_to_xpath(elements):
    return list(map(
        lambda x: get_element_xpath(x),
        elements
    ))


def map_to_action_list(element_xpaths, ActionClass, state):
    return list(map(
        lambda x: ActionClass(
            xpath=x,
            parent_state=state,
        ),
        element_xpaths
    ))


def find_form_actions(state):
    forms = workflow.find_forms()
    forms = filter_hidden_elements(forms)
    forms_xpath = map_elements_to_xpath(forms)
    forms_actions = map_to_action_list(forms_xpath, FormAction, state)
    return forms_actions


def find_click_actions(state):
    tags = driver.find_elements(By.TAG_NAME, 'a')
    tags = filter_hidden_elements(tags)
    tags_xpath = map_elements_to_xpath(tags)
    tags_actions = map_to_action_list(tags_xpath, ClickAction, state)
    return tags_actions


def find_hover_actions(state):
    return []