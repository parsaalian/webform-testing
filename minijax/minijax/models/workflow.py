from __future__ import annotations

from selenium.webdriver.remote.webelement import WebElement

from minijax.config import Config
from minijax.utils import Singleton

from .form_finder import find_forms_by_query
from .form_parser import basic_parse_form_inputs, ParseEntry
from minijax.models.value_generator import (
    rule_based_value_generator,
    gpt3_value_generator,
    chatgpt_value_generator,
)


cfg = Config()


class Workflow(metaclass=Singleton):
    def __init__(self):
        self.form_finder = None
        self.form_parser = None
        self.value_generator = None
        self.command_executor = None
    
    
    def find_form(self) -> WebElement:
        if self.form_finder is not None:
            return self.form_finder()

        if cfg.model_config['workflow']['finder'] == 'QUERY':
            self.form_finder = find_forms_by_query
        
        return self.form_finder()
    
    
    def parse_form(
        self,
        form: WebElement
    ) -> WebElement | list(ParseEntry):
        if self.form_parser is not None:
            return self.form_parser(form)

        if cfg.model_config['workflow']['parser'] == 'BASIC':
            self.form_parser = basic_parse_form_inputs(form)
        
        return self.form_parser(form)
    
    
    def generate_commands(
        self,
        form: WebElement | list(ParseEntry)
    ) -> str:
        if self.value_generator is not None:
            return self.value_generator(form)

        # Basic config
        if cfg.model_config['workflow']['filler'] == 'FIXED':
            self.value_generator = rule_based_value_generator(random=False)
        if cfg.model_config['workflow']['filler'] == 'RANDOM':
            self.value_generator = rule_based_value_generator(random=True)
        
        # GPT3 config
        if cfg.model_config['workflow']['filler'] == 'GPT3':
            self.value_generator = gpt3_value_generator(zero_shot=cfg.model_config['parameters']['zero_shot'])
        
        # Chat model config (GPT3.5 - GPT4)
        if cfg.model_config['workflow']['filler'] == 'GPT3.5' or cfg.model_config['workflow']['filler']:
            self.value_generator = chatgpt_value_generator(zero_shot=cfg.model_config['parameters']['zero_shot'])
        
        return self.value_generator(form)
    
    
    def execute_commands(self):
        pass