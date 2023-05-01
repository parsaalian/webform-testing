import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "http://localhost:8080"
driver.get(URL)

xpath_script = """
function getPathTo(element) {
    if (element.id !== '')
        return 'id(\"'+element.id+'\")';
    if (element === document.body)
        return element.tagName;
    var ix= 0;
    var siblings= element.parentNode.childNodes;
    for (var i= 0; i<siblings.length; i++) {
        var sibling= siblings[i];
        if (sibling===element)
            return getPathTo(element.parentNode) + '/' + element.tagName + '[' + (ix + 1) + ']';
        if (sibling.nodeType===1 && sibling.tagName===element.tagName)
            ix++;
    }
}
const path = getPathTo(arguments[0]);
if (path.startsWith('id(')) {
    return path;
}
return '//' + path;
"""

class Action:
    def __init__(self, action_element_xpath):
        self.element_xpath = action_element_xpath
    
    
    def perform(self):
        raise NotImplementedError("Action not implemented")
    
    
    def __str__(self):
        return f"Action {type(self)} at XPATH: {self.element_xpath}"
    
    
    def __eq__(self, other):
        return type(self) == type(other) and self.element_xpath == other.element_xpath


class GoToRootAction(Action):
    def __init__(self):
        pass
    
    
    def perform(self):
        driver.get(URL)


class ClickAction(Action):
    def __init__(self, click_element_xpath):
        super().__init__(click_element_xpath)
    
    
    def perform(self):
        element = driver.find_element(By.XPATH, self.element_xpath)
        element.click()


