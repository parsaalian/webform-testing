from selenium.webdriver.common.by import By


def find_forms_by_query(driver):
    forms = driver.find_elements(By.TAG_NAME, "form")
    return forms


__all__ = [
    'find_forms_by_query'
]