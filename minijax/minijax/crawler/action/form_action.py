from selenium.webdriver.common.by import By

from minijax.config import Config
from minijax.crawler import get_driver_container
from minijax.models.workflow import Workflow

from minijax.crawler.action.base import ActionBase


cfg = Config()
workflow = Workflow()
driver = get_driver_container().get_driver()


class FormAction(ActionBase):
    def __init__(self, xpath, parent_state):
        super().__init__(
            xpath,
            parent_state,
            execution_count=cfg.crawler_config['action']['form']['execution_count']
        )
    
    
    def should_execute_auth(self):
        return cfg.auth_config['has_auth'] and \
            self.parent_state.url == cfg.auth_config['auth_url'] and \
            self.xpath == cfg.auth_config['form_xpath']

    
    def execute_auth(self, form):
        username_xpath = cfg.auth_config['username_xpath']
        password_xpath = cfg.auth_config['password_xpath']
        username = cfg.auth_config['username']
        password = cfg.auth_config['password']
        form.find_element(By.XPATH, username_xpath).send_keys(username)
        form.find_element(By.XPATH, password_xpath).send_keys(password)
        return {
            username_xpath: username,
            password_xpath: password,
        }
    
    
    def execute(self):
        # find form step
        form = driver.find_element(By.XPATH, self.xpath)
        # fill/fill+parse step
        if self.should_execute_auth():
            values = self.execute_auth(form)
        else:
            values = workflow.execute(form)
        self.action_data = values
        # submit step
        result = submit_form(form)
    
    
    def retry(self):
        # find form step
        form = driver.find_element(By.XPATH, self.xpath)
        # fill/fill+parse step
        values = self.action_data
        workflow.execute_with_values(form, values)
        # submit step
        result = submit_form(form)
    
    
    def id(self):
        return f'{self.xpath} {str(self.execution_result)}'


# TODO: add submit form to workflow
def submit_form(form):
    submit_button = form.find_element(
        By.XPATH,
        '//button[@type = "submit"] | //input[@type = "submit"]'
    )
    submit_button.click()
    return True