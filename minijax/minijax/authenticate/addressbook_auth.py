from selenium.webdriver.common.by import By

from minijax.crawler.driver import get_driver_container


driver = get_driver_container().get_driver()


def authenticate_addressbook():
    driver.get('http://localhost:3000/addressbook/index.php')
    driver.find_element(By.XPATH, '//BODY/DIV[1]/DIV[4]/FORM[1]//INPUT[1]').send_keys('admin')
    driver.find_element(By.XPATH, '//BODY/DIV[1]/DIV[4]/FORM[1]//INPUT[2]').send_keys('secret')
    driver.find_element(By.XPATH, '//BODY/DIV[1]/DIV[4]/FORM[1]//INPUT[3]').click()