from __future__ import annotations

from selenium.webdriver.remote.webelement import WebElement

from minijax.config import Config
from minijax.utils import Singleton
from minijax.utils.functional import unity, compose
from minijax.crawler.utils import simplify_element

from .utils import (
    parse_generated_commands,
    execute_generated_commands,
    generate_commands_from_values
)
from .form_finder import find_forms_by_query
from .form_parser import (
    none_parse_form_inputs,
    basic_parse_form_inputs,
    ParseEntry,
)
from minijax.models.value_generator import (
    rule_based_value_generator,
    gpt3_value_generator,
    chat_gpt_value_generator,
)


cfg = Config()


class Workflow(metaclass=Singleton):
    def __init__(self):
        self.form_finder = None
        self.form_transformer = None
        self.form_parser = None
        self.value_generator = None
        self.command_executor = None
        
        self._check_workflow_validity()
    
    
    def _check_workflow_validity(self):
        invalid_combinations = [
            {
                'transformer': 'HTML',
                'parser': 'BASIC',
            },
            {
                'transformer': 'SIMPLIFY',
                'parser': 'BASIC',
            },
            {
                'parser': 'BASIC',
                'filler': 'GPT3',
            },
            {
                'parser': 'BASIC',
                'filler': 'GPT3.5',
            },
            {
                'parser': 'BASIC',
                'filler': 'GPT4',
            },
            {
                'parser': 'NONE',
                'filler': 'FIXED',
            },
            {
                'parser': 'NONE',
                'filler': 'RANDOM',
            },
        ]
        
        for invalid_combination in invalid_combinations:
            if all([
                cfg.model_config['workflow'][key] == value
                for key, value in invalid_combination.items()
            ]):
                raise Exception(f"Invalid workflow combination: {invalid_combination}")
    
    
    def find_forms(self) -> list(WebElement):
        if self.form_finder is not None:
            return self.form_finder()

        if cfg.model_config['workflow']['finder'] == 'QUERY':
            self.form_finder = find_forms_by_query
        
        return self.form_finder()
    
    
    def transform_form(
        self,
        form: WebElement
    ) -> str | WebElement:
        if self.form_transformer is not None:
            return self.form_transformer(form)

        if  cfg.model_config['workflow']['transformer'] == 'NONE':
            self.form_transformer = unity
        if cfg.model_config['workflow']['transformer'] == 'HTML':
            self.form_transformer = none_parse_form_inputs
        if cfg.model_config['workflow']['transformer'] == 'SIMPLIFY':
            self.form_transformer = simplify_element
        
        return self.form_transformer(form)
    
    
    def parse_form(
        self,
        form: WebElement
    ) -> str | list(ParseEntry):
        if self.form_parser is not None:
            return self.form_parser(form)
        
        if cfg.model_config['workflow']['parser'] == 'NONE':
            self.form_parser = unity
        elif cfg.model_config['workflow']['parser'] == 'BASIC':
            self.form_parser = basic_parse_form_inputs
        
        return self.form_parser(form)
    
    
    def generate_commands(
        self,
        parsed: str | list(ParseEntry)
    ) -> str:
        if self.value_generator is not None:
            return self.value_generator(parsed)

        # Basic config
        if cfg.model_config['workflow']['filler'] == 'FIXED':
            self.value_generator = rule_based_value_generator(random=False)
        elif cfg.model_config['workflow']['filler'] == 'RANDOM':
            self.value_generator = rule_based_value_generator(random=True)
        # GPT3 config
        elif cfg.model_config['workflow']['filler'] == 'GPT3':
            self.value_generator = gpt3_value_generator(zero_shot=cfg.model_config['parameters']['zero_shot'])
        # Chat model config (GPT3.5 - GPT4)
        elif cfg.model_config['workflow']['filler'] == 'GPT3.5' or cfg.model_config['workflow']['filler']:
            self.value_generator = chat_gpt_value_generator(zero_shot=cfg.model_config['parameters']['zero_shot'])
        
        return self.value_generator(parsed)
    
    
    def execute_commands(
        self,
        form: WebElement,
    ) -> function:
        def __wrapped(commands):
            values = execute_generated_commands(form, commands)
            return values
        return __wrapped

    
    def generate_commands_from_values(
        self,
        form: WebElement,
    ) -> function:
        def __wrapped(values):
            commands = generate_commands_from_values(form, values)
            return commands
        return __wrapped


    
    # TODO: add feedback loop
    def execute(
        self,
        form: WebElement,
    ) -> dict[str, str]:
        return compose(
            self.transform_form,
            self.parse_form,
            self.generate_commands,
            parse_generated_commands,
            self.execute_commands(form)
        )(form)
    
    
    def execute_with_values(
        self,
        form: WebElement,
        values: dict[str, str]
    ) -> dict[str, str]:
        return compose(
            self.generate_commands_from_values(form),
            self.execute_commands(form)
        )(values)