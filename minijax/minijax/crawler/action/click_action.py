from selenium.webdriver.common.by import By

from minijax.crawler import get_driver_container
from minijax.crawler.utils import get_element_xpath
from minijax.crawler.action.base import ActionBase


class ClickAction(ActionBase):
    def __init__(self, xpath):
        super().__init__(xpath)
    
    
    def execute(self):
        driver = get_driver_container().get_driver()
        element = driver.find_element(By.XPATH, self.xpath)
        element.click()
    
    
    def id(self):
        return self.xpath


def find_click_actions(driver):
    tags = driver.find_elements(By.TAG_NAME, 'a')
    tags = list(filter(lambda x: x.is_displayed(), tags))
    tags_xpath = list(map(
        lambda x: get_element_xpath(driver, x),
        tags
    ))
    tags_actions = list(map(
        lambda x: ClickAction(x),
        tags_xpath
    ))
    return tags_actions
