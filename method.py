#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().run_line_magic('load_ext', 'autoreload')
# get_ipython().run_line_magic('autoreload', '2')

import os
import time
import openai
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs

from method.ours.utils import create_driver, get_xpath, get_application_context
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
    get_local_feedback,
    get_global_feedback
)


# In[3]:


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Global Variables
HEADLESS = False
TEXT_EMBEDDING_METHOD = 'ADA'
GRAPH_EMBEDDING_METHOD = 'NODE2VEC'

URL = 'https://www.macys.com/'
# 'https://www.amazon.com/'
# 'https://www.carmax.com/'
# 'https://www.rei.com/'
# 'https://www.uhaul.com/'
# 'https://www.ups.com/us/en/Home.page'
# 'https://www.thumbtack.com/'
# 'https://www.healthgrades.com/'
# 'https://www.webmd.com/drugs/2/index'
# 'https://www.babycenter.com/child-height-predictor'
# 'https://www.babycenter.com/pregnancy-weight-gain-estimator'
# 'https://seatgeek.ca/'
# 'https://www.stubhub.ca/'
# 'https://app.invoicing.co/#/register'
# 'http://localhost:3000/default-channel/en-US/account/register/'
# 'http://localhost:9000/dashboard/discounts/sales/add'
# 'http://localhost:9000/dashboard/customers/add'
# 'http://localhost:8080/'
# 'https://www.budget.com/en/home'
# 'https://www.thetrainline.com/en-us'
# 'https://www.mbta.com/'
# 'https://resy.com/'
# 'https://www.yelp.com/'
# 'https://www.aa.com/homePage.do'
# 'https://www.jetblue.com/'
# 'https://www.united.com/en/us'
# 'https://www.aircanada.com/ca/en/aco/home.html'


def get_to_form(driver):
    try:
        driver.get(URL)
        
        '''
        # UPS - Quote
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tabs_0_tab_1'))
        ).click()
        '''
        
        '''
        # Saleor
        try:
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//BODY/DIV[1]/MAIN[1]/DIV[1]/DIV[1]/DIV[1]/FORM[1]/DIV[2]/DIV[1]/INPUT[1]')
                )
            ).send_keys('admin@example.com')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//BODY/DIV[1]/MAIN[1]/DIV[1]/DIV[1]/DIV[1]/FORM[1]/DIV[4]/DIV[1]/DIV[1]/INPUT[1]')
                )
            ).send_keys('admin')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//BODY/DIV[1]/MAIN[1]/DIV[1]/DIV[1]/DIV[1]/FORM[1]/DIV[5]/BUTTON[1]')
                )
            ).click()
        except:
            pass
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//BODY/DIV[1]/MAIN[1]/DIV[1]/DIV[2]/MAIN[1]/FORM[1]/DIV[1]/DIV[2]/DIV[4]/DIV[2]/LABEL[1]/SPAN[1]/SPAN[1]/INPUT[1]')
            )
        ).click()
        '''
        
        '''
        # Pet Clinic - Add Owner
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//BODY/APP-ROOT[1]/DIV[1]/NAV[1]/DIV[1]/UL[1]/LI[2]')
            )
        ).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//BODY/APP-ROOT[1]/DIV[1]/NAV[1]/DIV[1]/UL[1]/LI[2]/UL[1]/LI[2]')
            )
        ).click()
        '''
        
        '''
        # Budget - Reservation
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'PicLoc_value'))
        ).click()
        '''
        
        '''
        # MBTA
        time.sleep(2)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//BODY/DIV[1]/DIV[2]/MAIN[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]/A[1]'))
        ).click()
        '''
        
        '''
        # AC - My Bookings
        time.sleep(2)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'bkmg-tab-button-mngBook'))
        ).click()
        '''
        
        '''
        # AC - Multi-city
        time.sleep(2)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'bkmgFlights_tripTypeSelector_M'))
        ).click()
        '''
        
    except:
        print('timeout')


def find_form():
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//BODY/HEADER[1]/DIV[2]/DIV[1]/DIV[1]/SECTION[2]/DIV[2]/FORM[1]'
        ))
    )


def find_button():
    return None


# In[4]:


driver = create_driver(HEADLESS)
get_to_form(driver)


# In[5]:


form = find_form()


# In[6]:


history_table = HistoryTable(
    url=URL,
    xpath=get_xpath(driver, form)
)


# In[7]:


for element in form.find_elements(By.TAG_NAME, 'input'):
    try:
        element.clear()
    except:
        pass


# # Processing

# In[8]:


html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
relation_graph, input_groups = parse_form(
    driver,
    form,
    TEXT_EMBEDDING_METHOD=TEXT_EMBEDDING_METHOD
)


# # Generation

# In[9]:


def create_ablation_inclusion(mode='NORMAL'):
    no_ferg = mode == 'NOFERG'
    context = mode == 'CONTEXT'
    no_date = mode == 'NODATE'
    no_feedback = mode == 'NOFEEDBACK'
    
    return {
        'relevant': not no_ferg,
        'context': context,
        'date': not no_date,
        'constraints': False,
        'feedback': not no_feedback
    }


ablation_inclusion = create_ablation_inclusion(mode='NORMAL')


# In[10]:


try:
    app_context = get_application_context(driver)
except:
    app_context = ''


# In[11]:


value_table = generate_constraints_for_input_groups(
    input_groups,
    app_context=app_context,
    ablation_inclusion=ablation_inclusion
)


# In[12]:


value_table.print()


# In[13]:


value_table = generate_values_for_input_groups(
    input_groups,
    value_table,
    app_context=app_context,
    ablation_inclusion=ablation_inclusion
)


# In[14]:


fill_form_with_value_table(driver, value_table, input_groups)


# In[14]:


submit_form(driver, input_groups=input_groups, explicit_submit=find_button())


# In[15]:


new_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
global_feedback = get_global_feedback(html, new_html, remove_form_children=False)


# In[16]:


history_table.add(
    value_table.get_values_dict(),
    'base',
    global_feedback,
    driver.current_url
)


# # Feedback

# In[17]:


new_form = find_form()


# In[18]:


new_relation_graph, new_input_groups = parse_form(
    driver,
    new_form,
    prev_relation_graph=relation_graph,
    TEXT_EMBEDDING_METHOD=TEXT_EMBEDDING_METHOD
)


# In[19]:


global_feedback = get_global_feedback(html, new_html, remove_form_children=True)


# In[20]:


global_feedback


# In[21]:


value_table = generate_constraints_for_input_groups(
    new_input_groups,
    value_table,
    global_feedback,
    app_context=app_context,
    ablation_inclusion=ablation_inclusion
)


# In[22]:


value_table.print()


# In[24]:


value_table = generate_values_for_input_groups(
    new_input_groups,
    value_table,
    global_feedback=global_feedback,
    app_context=app_context,
    ablation_inclusion=ablation_inclusion
)


# In[25]:


fill_form_with_value_table(driver, value_table, new_input_groups)


# In[29]:


submit_form(driver, input_groups=new_input_groups, explicit_submit=find_button())


# In[27]:


new_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
global_feedback = get_global_feedback(html, new_html, remove_form_children=False)

history_table.add(
    value_table.get_values_dict(),
    'base',
    global_feedback,
    driver.current_url
)


# # Constraint Negation

# In[18]:


form_context = get_form_context(input_groups)


# In[19]:


# history_table.table = history_table.table[:1]


# In[21]:


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
            context=form_context
        )

        # fill_form_with_value_table(driver, value_table_copy, input_groups)

        try:
            pass
            # driver.find_element(By.TAG_NAME, 'body').click()
            # submit_form(driver, input_groups=input_groups, explicit_submit=find_button())
        except:
            pass
        
        # time.sleep(1)
        
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


# In[21]:


'''driver.get(URL)
time.sleep(1)
base_text = driver.find_element(By.TAG_NAME, 'body').text'''


# In[20]:


for i, v in enumerate(history_table.table['values']):
    jv = json.loads(v)
    for key, value in jv.items():
        if key not in history_table.table.columns:
            history_table.table[key] = None
        history_table.table.loc[i, key] = value


# In[21]:


history_table.table


# In[49]:


history_table.table = history_table.table[
    history_table.table.feedback.str.len() < len(base_text)
]


# In[31]:


set('FEEDBACK-DELIMITER'.join(history_table.table.feedback).split('FEEDBACK-DELIMITER'))


# In[34]:


len(set('FEEDBACK-DELIMITER'.join(history_table.table.feedback).split('FEEDBACK-DELIMITER')))


# In[23]:


history_table.to_test_case('aoc-multitrip.py')