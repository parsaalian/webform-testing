#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

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


# In[2]:


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Global Variables
HEADLESS = False
TEXT_EMBEDDING_METHOD = 'ADA'
GRAPH_EMBEDDING_METHOD = 'NODE2VEC'

URL = 'https://seatgeek.ca/'
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
            '//BODY/DIV[2]/NAV[1]/DIV[2]/DIV[1]/FORM[1]'
        ))
    )


def find_button():
    return None


# In[3]:


from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig

def load_model_llama(model_type, use_triton=False):
    if model_type == '70B':
        model_name_or_path = "TheBloke/Llama-2-70B-chat-GPTQ"
        model_basename = "gptq_model-4bit--1g"
    elif model_type == '13B':
        model_name_or_path = "TheBloke/Llama-2-13B-chat-GPTQ"
        model_basename = "gptq_model-4bit-128g"
    else:
        raise ValueError('Invalid model_type. Choose either "70B" or "13B".')

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True, device_map="auto")

    model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
                                               model_basename=model_basename,
                                               inject_fused_attention=False,
                                               use_safetensors=True,
                                               trust_remote_code=False,
                                               use_triton=use_triton,
                                               quantize_config=None)
    return tokenizer, model


# Load the model - load_model_llama2_70b
tokenizer, model = load_model_llama("70B")


# In[4]:


driver = create_driver_server(HEADLESS)
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

# In[ ]:


try:
    app_context = get_application_context(driver)
except:
    app_context = ''


# In[10]:


value_table = generate_constraints_for_input_groups(
    input_groups,
    app_context=app_context,
    model=model,
    tokenizer=tokenizer,
)


# In[13]:


value_table.print()


# In[ ]:


value_table = generate_values_for_input_groups(
    input_groups,
    value_table,
    app_context=app_context,
    model=model,
    tokenizer=tokenizer,
)


# In[14]:


fill_form_with_value_table(driver, value_table, input_groups)


# In[15]:


submit_form(driver, input_groups=input_groups, explicit_submit=find_button())


# In[16]:


new_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')
global_feedback = get_global_feedback(html, new_html, remove_form_children=False)


# In[17]:


history_table.add(
    value_table.get_values_dict(),
    'base',
    global_feedback,
    driver.current_url
)

