import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from app_navigator.custom_navigator import navigate_to_claroline_form as navigate_to_page
from form_finder.simple_form_finder import find_form_by_tag as find_form
from form_parser.simple_form_parser import parse_form_inputs_without_labels as parse_form
from form_filler.simple_form_filler import fill_form_with_fixed_values as fill_and_submit_form


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

navigate_to_page(driver)

form = find_form(driver)

parsed_form = parse_form(form)

fill_and_submit_form(parsed_form)

'''
feedback = find_feedback(driver, form)

while feedback is not None:
    form = find_form(driver)
    parsed_form = parse_form(form)
    fill_and_submit_form(parsed_form, feedback)
    feedback = find_feedback(driver, form)
'''

time.sleep(2)
driver.quit()