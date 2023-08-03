import os
import time
import copy
import json
import openai
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from method.models import generate_random_values, generate_static_values, generate_llm_values
from method.ours.utils import create_driver, get_xpath, interact_with_input
from method.ours.history import HistoryTable
from method.ours.feedback import get_global_feedback


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Global Variables
HEADLESS = False
METHOD = 'llm'
URL = 'https://www.aircanada.com/ca/en/aco/home.html'


def get_to_form(driver):
    try:
        driver.get(URL)
    except:
        print('timeout')


def find_form():
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//BODY/AC-WEB-APP[1]/DIV[1]/MAIN[1]/DIV[1]/AC-ACOHOME-PAGE[1]/DIV[1]/DIV[1]/AC-BOOKING-MAGNET[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/AC-BKMG-FLIGHTS-TAB[1]/DIV[1]/FORM[1]'
        ))
    )

def find_button():
    '''
    return find_form().find_element(
        By.XPATH,
        '//BODY/DIV[1]/DIV[3]/DIV[1]/DIV[5]/DIV[1]/DIV[1]/ARTICLE[1]/DIV[2]/DIV[1]/DIV[1]/DIV[2]/DIV[2]/BUTTON[1]'
    )
    '''
    return None


driver = create_driver(HEADLESS)
get_to_form(driver)


html = driver.find_element(By.TAG_NAME, 'html').get_attribute('outerHTML')
form = find_form()
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
elif METHOD == 'random':
    values = generate_random_values(driver, inputs)
else:
    values = generate_llm_values(form.get_attribute('outerHTML'), openai.api_key)


def get_element(element_id):
    return driver.find_element(By.ID if METHOD == 'llm' else By.XPATH, element_id)


def send_values(element_ids, values):
    for element_id in element_ids:
        try:
            element = get_element(element_id)
        except:
            continue
        value = values[element_id]
        
        element_type = element.get_attribute('type') or 'text'
    
        if element_type in ['radio', 'checkbox'] or element.tag_name in ['button']:
            continue
        
        try:
            interact_with_input(element, value)
        except:
            pass

        
def submit_form(form):
    submit = find_button()
    
    for _ in range(3):
        try:
            interact_with_input(submit, True)
            time.sleep(0.5)
        except:
            break


passing_set = {
    element_id: values[element_id]['passing'] for element_id in values.keys()
}


for element_id, element_values in values.items():
    get_to_form(driver)
    time.sleep(1)
    
    try:
        element = get_element(element_id)
    except:
        continue
    element_type = element.get_attribute('type') or 'text'
    
    if element_type in ['radio', 'checkbox', 'submit']:
        continue
    
    for failing_value in element_values['failing']:
        try:
            get_to_form(driver)
            time.sleep(1)
        
            passing_copy = copy.copy(passing_set)
            passing_copy[element_id] = failing_value
            send_values(values.keys(), passing_copy)

            time.sleep(1)

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


for i, v in enumerate(history_table.table['values']):
    jv = json.loads(v)
    for key, value in jv.items():
        if key not in history_table.table.columns:
            history_table.table[key] = None
        history_table.table.loc[i, key] = value


history_table.table.to_csv(f'./data/{METHOD}.csv', index=False)