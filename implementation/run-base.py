import os
import time
import copy
import json
import openai
from dotenv import load_dotenv

from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

from method.models import generate_random_values, generate_static_values, generate_llm_values
from method.ours.utils import create_driver, get_xpath, interact_with_input
from method.ours.history import HistoryTable
from method.ours.feedback import get_global_feedback


METHOD = 'static' # or 'random'


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

HEADLESS = False
URL = 'https://www.aircanada.com/ca/en/aco/home.html'


def get_to_form():
    driver = create_driver(HEADLESS)
    driver.get(URL)
    
    # additional step to get to the form
    
    return driver


driver = get_to_form()


html = driver.find_element(By.TAG_NAME, 'html').get_attribute('outerHTML')
form = driver.find_elements(By.TAG_NAME, 'form')[1]
form_xpath = get_xpath(driver, form)


inputs = form.find_elements(
    By.XPATH,
    f'{form_xpath}//input | {form_xpath}//textarea | {form_xpath}//select'
)
inputs = list(filter(
    lambda x: x.get_attribute('type') != 'hidden' and x.get_attribute('hidden') != 'true',
    inputs
))


history_table = HistoryTable(
    url=URL,
    xpath=form_xpath
)

values = None
if METHOD == 'static':
    values = generate_static_values(driver, inputs)
else:
    values = generate_random_values(driver, inputs)


def send_values(elements, values):
    for element_id in elements.keys():
        element = elements[element_id]
        value = values[element_id]
        
        element_type = element.get_attribute('type') or 'text'
    
        if element_type in ['radio', 'checkbox'] or element.tag_name in ['button']:
            continue
        
        interact_with_input(element, value)


def submit_form(form):
    submit = form.find_element(By.XPATH, f'{form_xpath}//*[@type="submit"]')
    
    for _ in range(3):
        try:
            interact_with_input(submit, True)
            time.sleep(0.5)
        except:
            break


passing_set = {
    element_id: values[element_id]['passing'] for element_id in values.keys()
}

elements = {
    element_id: driver.find_element(By.XPATH, element_id) for element_id in values.keys()
}


for element_id, element_values in values.items():
    element = elements[element_id]
    element_type = element.get_attribute('type') or 'text'
    
    if element_type in ['radio', 'checkbox']:
        continue
    
    for failing_value in element_values['failing']:
        try:
            passing_copy = copy.copy(passing_set)
            passing_copy[element_id] = failing_value
            send_values(elements, passing_copy)

            time.sleep(2)

            submit_form(form)

            new_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
            global_feedback = get_global_feedback(html, new_html, remove_form_children=False)

            history_table.add(
                passing_copy,
                'base',
                global_feedback,
                driver.current_url
            )
        except Exception as e:
            print(e)