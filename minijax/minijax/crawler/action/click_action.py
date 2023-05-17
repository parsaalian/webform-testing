from selenium.webdriver.common.by import By

from minijax.crawler import get_driver_container
from minijax.crawler.action.base import ActionBase


class ClickAction(ActionBase):
    def __init__(self, xpath, parent_state):
        super().__init__(xpath, parent_state)
    
    
    def execute(self):
        driver = get_driver_container().get_driver()
        element = driver.find_element(By.XPATH, self.xpath)
        element.click()
    
    
    def id(self):
        return self.xpath
