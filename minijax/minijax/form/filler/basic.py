import rstr
import random

from selenium.webdriver.support.ui import Select

from minijax.crawler.driver import get_driver_container
from minijax.crawler.utils import get_element_xpath


def fill_form_with_fixed_values(parsed_form):
    driver = get_driver_container().get_driver()
    values = {}
    
    for i in parsed_form:
        element = i['element']
        xpath = get_element_xpath(driver, element)
        
        if i['tag'] == 'button':
            continue
        
        if i['tag'] == 'select':
            select = Select(element)
            select.select_by_index(0)
        
        elif i['attributes']['type'] == 'number':
            element.send_keys('0')
        
        elif i['attributes']['type'] == 'checkbox' or i['attributes']['type'] == 'radio':
            try:
                element.click()
            except:
                pass
        
        elif i['attributes']['type'] == 'text':
            try:
                element.send_keys('test')
            except:
                pass
        
        values[xpath] = element.get_attribute('value')
    
    return values


def fill_form_with_random_values(parsed_form):
    driver = get_driver_container().get_driver()
    values = {}
    
    for i in parsed_form:
        element = i['element']
        xpath = get_element_xpath(driver, element)
        
        if i['tag'] == 'button':
            continue
        
        if i['tag'] == 'select':
            select = Select(element)
            select.select_by_index(random.randint(0, len(select.options) - 1))
        
        elif i['attributes']['type'] == 'number':
            element.send_keys(random.randint(0, 1000))
        
        elif i['attributes']['type'] == 'checkbox' or i['attributes']['type'] == 'radio':
            try:
                if random.randint(0, 1) == 0:
                    element.click()
            except:
                pass
        
        elif i['attributes']['type'] == 'text':
            try:
                element.send_keys(rstr.xeger(r'[A-Za-z0-9]{10}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'email':
            try:
                element.send_keys(rstr.xeger(r'[A-Za-z0-9]{10}') + '@' + rstr.xeger(r'[A-Za-z0-9]{10}') + '.com')
            except:
                pass
        
        elif i['attributes']['type'] == 'password':
            try:
                element.send_keys(rstr.xeger(r'[A-Za-z0-9]{10}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'date':
            try:
                element.send_keys(rstr.xeger(r'[0-9]{4}') + '-' + rstr.xeger(r'[0-9]{2}') + '-' + rstr.xeger(r'[0-9]{2}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'time':
            try:
                element.send_keys(rstr.xeger(r'[0-9]{2}') + ':' + rstr.xeger(r'[0-9]{2}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'datetime-local':
            try:
                element.send_keys(rstr.xeger(r'[0-9]{4}') + '-' + rstr.xeger(r'[0-9]{2}') + '-' + rstr.xeger(r'[0-9]{2}') + 'T' + rstr.xeger(r'[0-9]{2}') + ':' + rstr.xeger(r'[0-9]{2}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'tel':
            try:
                element.send_keys(rstr.xeger(r'[0-9]{10}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'url':
            try:
                element.send_keys('https://' + rstr.xeger(r'[A-Za-z0-9]{10}') + '.com')
            except:
                pass
        
        elif i['attributes']['type'] == 'week':
            try:
                element.send_keys(rstr.xeger(r'[0-9]{4}') + '-' + rstr.xeger(r'[0-9]{2}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'month':
            try:
                element.send_keys(rstr.xeger(r'[0-9]{4}') + '-' + rstr.xeger(r'[0-9]{2}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'color':
            try:
                element.send_keys('#' + rstr.xeger(r'[0-9A-Fa-f]{6}'))
            except:
                pass
        
        elif i['attributes']['type'] == 'range':
            try:
                element.send_keys(random.randint(0, 100))
            except:
                pass
        
        values[xpath] = element.get_attribute('value')
    
    return values
