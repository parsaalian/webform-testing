#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


import os
import time
import copy
import json
import openai
from dotenv import load_dotenv

from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from method.models import generate_random_values, generate_static_values, generate_llm_values, generate_llm_values_llama
from method.ours.utils import create_driver_server, get_xpath, interact_with_input
from method.ours.history import HistoryTable
from method.ours.feedback import get_global_feedback


# In[2]:


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Global Variables
HEADLESS = False
TEXT_EMBEDDING_METHOD = 'ADA' # ['ADA', 'WORD2VEC', 'SPACY']
GRAPH_EMBEDDING_METHOD = 'NODE2VEC' # ['NODE2VEC', 'GCN']

# URL = 'https://www.ups.com/ca/en/Home.page'
# 'https://www.healthgrades.com/find-a-doctor'
# 'https://www.babycenter.com/child-height-predictor'
# 'https://www.babycenter.com/pregnancy-weight-gain-estimator'
# 'https://www.yelp.com/'
# URL = 'https://www.aircanada.com/ca/en/aco/home.html'
# 'https://app.invoicing.co/#/register'
# 'http://localhost:8080/1/common/items/create'
# 'http://localhost:3000/default-channel/en-US/account/register/'
# 'http://localhost:9000/dashboard/discounts/sales/add'
# 'http://localhost:9000/dashboard/customers/add'
# 'https://www.mbta.com/'
# 'https://www.united.com/en/us'
# 'https://www.uhaul.com/Truck-Rentals/'

# URL = 'https://seatgeek.ca/'
# 'https://www.stubhub.ca/'
# 'https://www.thetrainline.com/en-us'
# 'https://resy.com/'
# 'https://www.aa.com/homePage.do' 
# 'https://www.jetblue.com/'
# 'https://www.united.com/en/us'
# 'https://www.tripadvisor.ca/'
# 'https://www.webmd.com/drugs/2/index'
# 'https://www.thumbtack.com/'
# 'https://www.rei.com/'
# 'https://www.carmax.com/'
# 'https://www.amazon.ca/'
URL = 'https://www.macys.com/'


def get_to_form(driver):
    try:
        driver.get(URL)
    except:
        print('timeout')
    
    # UPS - Quote
    #time.sleep(2)
    #WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.ID, 'tabs_0_tab_1'))
    #).click()
    
    # AC - Multi-city
    time.sleep(2)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'bkmgFlights_tripTypeSelector_M'))
    ).click()    
    
    '''
    # Budget - Reservation
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'PicLoc_value'))
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
    
    '''
    # Akaunting
    try:
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.ID,
                'email')
            )
        ).send_keys('me@company.com')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.ID,
                'password')
            )
        ).send_keys('password')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//*[@type="submit"]')
            )
        ).click()
    except:
        pass
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
    '''

    '''
    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//BODY/DIV[1]/DIV[2]/MAIN[1]/DIV[1]/DIV[1]/DIV[1]/DIV[2]')
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
        '/html/body/ac-web-app/div/main/div[1]/ac-acohome-page/div/div/ac-booking-magnet/div/div/div/div[2]/ac-bkmg-flights-tab/div/form/fieldset/div/div[2]/abc-button'
    )
    '''
    # return driver.find_elements(By.TAG_NAME, 'button')[10]
    return None


# In[3]:


METHOD = 'llama'


# In[4]:


driver = create_driver_server(HEADLESS)
get_to_form(driver)


# In[5]:


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


# In[6]:


history_table = HistoryTable(
    url=URL,
    xpath=form_xpath
)


# In[7]:


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


# In[8]:


values = None
if METHOD == 'static':
    values = generate_static_values(driver, inputs)
elif METHOD == 'random':
    values = generate_random_values(driver, inputs)
elif METHOD == 'llama':
    values = generate_llm_values_llama(form.get_attribute('outerHTML'), model, tokenizer)    
else:
    values = generate_llm_values(form.get_attribute('outerHTML'), openai.api_key)


# In[9]:


model


# In[10]:


print(values)