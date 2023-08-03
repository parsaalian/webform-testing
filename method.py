import os
import time
import json
import openai
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from method.ours.utils import create_driver, get_xpath
from method.ours.parse import parse_form
from method.ours.prompts import get_form_context
from method.ours.history import HistoryTable
from method.ours.constraints import Invalid
from method.ours.generation import (
    generate_constraints_for_input_groups,
    generate_value_for_input_group,
    generate_values_for_input_groups,
    fill_form_with_value_table,
    submit_form
)
from method.ours.feedback import (
    get_global_feedback
)


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Global Variables
HEADLESS = False
TEXT_EMBEDDING_METHOD = 'ADA' # ['ADA', 'WORD2VEC', 'SPACY']
GRAPH_EMBEDDING_METHOD = 'NODE2VEC' # ['NODE2VEC', 'GCN']

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


form = find_form()


history_table = HistoryTable(
    url=URL,
    xpath=get_xpath(driver, form)
)


for element in form.find_elements(By.TAG_NAME, 'input'):
    try:
        element.clear()
    except:
        pass


html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
relation_graph, input_groups = parse_form(
    driver,
    form,
    TEXT_EMBEDDING_METHOD=TEXT_EMBEDDING_METHOD
)


constraint_ablation = {
    'relevant': True,
    'context': True,
    'constraints': True,
    # do not edit
    'feedback': True,
}

value_ablation = {
    'input_group': True,
    'context': True,
    # do not edit
    'constraints': True,
    'related': True,
}


value_table = generate_constraints_for_input_groups(
    input_groups,
    ablation_inclusion=constraint_ablation
)


value_table = generate_values_for_input_groups(
    input_groups,
    value_table,
    ablation_inclusion=value_ablation
)


fill_form_with_value_table(driver, value_table, input_groups)


submit_form(driver, input_groups=input_groups, explicit_submit=find_button())


new_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
global_feedback = get_global_feedback(html, new_html, remove_form_children=False)


history_table.add(
    value_table.get_values_dict(),
    'base',
    global_feedback,
    driver.current_url
)


## Feedback
new_form = find_form()


new_relation_graph, new_input_groups = parse_form(
    driver,
    new_form,
    prev_relation_graph=relation_graph,
    TEXT_EMBEDDING_METHOD=TEXT_EMBEDDING_METHOD
)


global_feedback = get_global_feedback(html, new_html, remove_form_children=True)


value_table = generate_constraints_for_input_groups(
    new_input_groups,
    value_table,
    global_feedback,
    ablation_inclusion=constraint_ablation
)


value_table = generate_values_for_input_groups(
    new_input_groups,
    value_table,
    ablation_inclusion=value_ablation
)


fill_form_with_value_table(driver, value_table, new_input_groups)


submit_form(driver, input_groups=new_input_groups, explicit_submit=find_button())


new_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
global_feedback = get_global_feedback(html, new_html, remove_form_children=False)

history_table.add(
    value_table.get_values_dict(),
    'base',
    global_feedback,
    driver.current_url
)


form_context = get_form_context(input_groups)


get_attr = lambda x, a, d: x[a] if a in x else d

for field_id, entry in value_table.entries.items():
    input_type = get_attr(entry.input_group.node.element.attrs, 'type', 'text')
    if input_type in ['radio', 'checkbox']:
        continue
    
    for i in range(len(entry.constraints) + 1):
        get_to_form(driver)
        
        value_table_copy = value_table.copy()
    
        if i == 0:
            value_table_copy.entries[field_id].constraints = [Invalid()]
        else:
            value_table_copy.entries[field_id].constraints = [value_table.entries[field_id].constraints[i - 1].copy()]
            value_table_copy.entries[field_id].constraints[0].flip_negative()


        input_group = value_table_copy.entries[field_id].input_group

        value_table_copy = generate_value_for_input_group(
            input_group,
            value_table_copy,
            form_context=form_context
        )

        fill_form_with_value_table(driver, value_table_copy, input_groups)

        try:
            driver.find_element(By.TAG_NAME, 'body').click()
            submit_form(driver, input_groups=input_groups, explicit_submit=find_button())
        except:
            pass
        
        time.sleep(1)
        
        new_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
        global_feedback = get_global_feedback(html, new_html)
        
        print(global_feedback)
        
        history_table.add(
            value_table_copy.get_values_dict(),
            str(type(value_table_copy.entries[field_id].constraints[0])),
            global_feedback,
            driver.current_url
        )
        
        if len(global_feedback) == 0:
            value_table.entries[field_id].constraints[i - 1].approve()


for i, v in enumerate(history_table.table['values']):
    jv = json.loads(v)
    for key, value in jv.items():
        if key not in history_table.table.columns:
            history_table.table[key] = None
        history_table.table.loc[i, key] = value


history_table.to_test_case('aoc-round-trip.py')
