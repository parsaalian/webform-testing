import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


class FormTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver.get(URL)
    
    
    def tearDown(self):
        self.driver.close()
    
    
    # get name from values variation
    def test_something(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        # fill values in form
        # element = WebDriverWait(driver, 5).until(
        #   EC.presence_of_element_located((By.ID, "id-of-new-element"))
        # )
        # submit the form
        # assert the feedback url and feedback if any
        # save the dom and the screenshots


if __name__ == "__main__":
    unittest.main()


test_file_template = '''
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


class FormTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver.get(URL)
    
    
    def tearDown(self):
        self.driver.close()
    
    
    {test_cases}


if __name__ == "__main__":
    unittest.main()
'''


test_case_template = '''
def test_{name}(self):
    \'\'\'{description}\'\'\'
    driver = self.driver
    {code}
'''