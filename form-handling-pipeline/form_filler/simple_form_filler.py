import time
from selenium.webdriver.support.ui import Select


def fill_form_with_fixed_values(parsed_form):
    for i in parsed_form:
        element = i['element']
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
                print(element.get_attribute('outerHTML'))
    
    submit = list(filter(
        lambda x: x['attributes']['type'] == 'submit',
        parsed_form
    ))[0]["element"]
    
    submit.click()