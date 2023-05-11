from minijax.utils import AbstractSingleton

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverContainer(AbstractSingleton):
    def __init__(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = driver
    
    
    def get_driver(self):
        return self.driver


def get_driver_container():
    driver_container = DriverContainer()
    return driver_container
