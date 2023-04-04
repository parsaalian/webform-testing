from selenium.webdriver.common.by import By


class FormParser:
    def __init__(self, selenium_form_element):
        self.element = selenium_form_element


    def parse_form(self):
        pass


class SimplestFormParser(FormParser):
    def parse_form(self):
        return {
            'action': self.element.get_attribute('action'),
            'method': self.element.get_attribute('method'),
            'inputs': self._parse_inputs()
        }


    def _parse_inputs(self):
        inputs = self.element.find_elements(By.TAG_NAME, 'input')
        labels = self.element.find_elements(By.TAG_NAME, 'label')
        return [self._parse_input(inputs[i], labels[i]) for i in range(len(inputs))]


    def _parse_input(self, inp, label):
        return {
            'element': inp,
            'label': label.text,
            'type': inp.get_attribute('type'),
            'value': inp.get_attribute('value')
        }