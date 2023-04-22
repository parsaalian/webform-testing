from selenium.webdriver.common.by import By


def find_form_by_tag(driver):
    form = driver.find_element(By.TAG_NAME, 'form')
    return form
