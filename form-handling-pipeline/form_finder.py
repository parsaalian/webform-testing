from selenium.webdriver.common.by import By


class FormFinder:
    def __init__(self, driver):
        self.driver = driver
    
    
    def find_form(self):
        pass


class SimplestFormFinder(FormFinder):
    def find_form(self):
        try:
            return self.driver.find_element(By.TAG_NAME, 'form')
        except:
            return None