from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from minijax.crawler import get_driver_container
from minijax.crawler.action.base import ActionBase


def find_hover_actions(driver):
    return []


class HoverAction(ActionBase):
    def __init__(self, action_element_xpath):
        super().__init__(action_element_xpath)
    
    
    def execute(self):
        driver = get_driver_container().get_driver()
        action = ActionChains(driver);
        node = driver.find_element(By.XPATH, self.xpath)
        action.move_to_element(node).perform()
