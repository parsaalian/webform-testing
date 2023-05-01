from selenium.webdriver.common.by import By


def navigate_to_claroline_form(driver):
    driver.get("http://localhost:3000/claroline11110/")
    login_form = driver.find_element(By.CLASS_NAME, "claroLoginForm")
    username_input, password_input = login_form.find_elements(By.TAG_NAME, "input")
    submit_button = login_form.find_element(By.TAG_NAME, "button")
    
    username_input.send_keys("admin")
    password_input.send_keys("admin")
    submit_button.click()
    
    driver.get("http://localhost:3000/claroline11110/claroline/course/create.php")