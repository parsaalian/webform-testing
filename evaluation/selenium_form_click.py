from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_driver():
    webdriver_service = Service(ChromeDriverManager().install())

    options = Options()
    #options.add_argument('--headless') # Optional argument to run the browser in headless mode

    driver = webdriver.Chrome(service=webdriver_service, options=options)
    return driver

def navigate_and_click_form(url, form_xpath, input_fields, driver):
    # Go to the URL
    driver.get(url)

    print("Filling input fields...")
    for name, value in input_fields.items():
        input_field = driver.find_element(By.NAME, name)
        input_field.send_keys(value)

    # Find the form and click on it
    form_element = driver.find_element(By.XPATH, form_xpath)
    form_element.click()
    print("Finished the process. Keeping the browser open for review...")

try:
    print("start")
    driver = get_driver()
    input_fields = {'user': 'my_username', 'pass': 'my_password'}
    navigate_and_click_form('http://localhost:3000/addressbook/index.php', "//input[@type='submit']", input_fields, driver)
    input("Press Enter to exit...")
    #driver.quit()  # Close the browser
except Exception as e:
    print("An error occurred:")
    print(e)
