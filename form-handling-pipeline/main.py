import os
import time
import argparse
from dotenv import load_dotenv

import openai

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from form_finder import SimplestFormFinder
from form_parser import SimplestFormParser
from form_filler import SimplestFormFiller, GPT3SimpleFormFiller


load_dotenv()


parser = argparse.ArgumentParser(
    description="Form Handling Pipeline",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("--url", type=str, default="http://localhost:8080")
args = parser.parse_args()
config = vars(args)


URL = config["url"]
# MODEL = "text-davinci-003"
MODEL = "text-ada-001"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)
openai.api_key = os.getenv("OPENAI_API_KEY")

driver.find_element(By.CLASS_NAME, 'navbar-nav').find_element(By.CLASS_NAME, 'dropdown').click()
driver.find_element(By.CLASS_NAME, 'navbar-nav') \
        .find_element(By.CLASS_NAME, 'dropdown') \
        .find_element(By.TAG_NAME, 'ul') \
        .find_element(By.TAG_NAME, 'li').click()

form_finder = SimplestFormFinder(driver)
form = form_finder.find_form()
form_parser = SimplestFormParser(form)
form_data = form_parser.parse_form()
form_filler = GPT3SimpleFormFiller(form_data, model=MODEL)
filled_form = form_filler.fill_form()


time.sleep(5)
driver.quit()