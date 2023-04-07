import os
import time
import argparse
from dotenv import load_dotenv

import openai

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from page_transformer import driver_to_doc, simplify_doc


# Initial configurations
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


parser = argparse.ArgumentParser(
    description="Form Handling Pipeline",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("--url", type=str, default="http://localhost:8080")
parser.add_argument("--gpt-model", type=str, default="text-davinci-003")
args = parser.parse_args()
config = vars(args)

URL = config["url"]
MODEL = config["gpt_model"]

# Run Selenium driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)


# OPTIONAL: Navigate to the form page
driver.find_element(By.CLASS_NAME, 'navbar-nav').find_element(By.CLASS_NAME, 'dropdown').click()
driver.find_element(By.CLASS_NAME, 'navbar-nav') \
        .find_element(By.CLASS_NAME, 'dropdown') \
        .find_element(By.TAG_NAME, 'ul') \
        .find_element(By.TAG_NAME, 'li').click()


# Run the pipeline
doc = driver_to_doc(driver)
doc = simplify_doc(doc)


'''form_finder = SimplestFormFinder(driver)
form = form_finder.find_form()
form_parser = SimplestFormParser(form)
form_data = form_parser.parse_form()
form_filler = GPT3SimpleFormFiller(form_data, model=MODEL)
filled_form = form_filler.fill_form()'''


# Quit the driver

time.sleep(1)
driver.quit()
