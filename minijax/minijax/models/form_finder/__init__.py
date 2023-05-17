from selenium.webdriver.common.by import By

from minijax.crawler.driver import get_driver_container


def find_forms_by_query():
    driver = get_driver_container().get_driver()
    forms = driver.find_elements(By.TAG_NAME, "form")
    return forms


__all__ = [
    'find_forms_by_query'
]