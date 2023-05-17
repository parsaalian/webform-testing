from minijax.config import Config
from minijax.llm.openai import ApiManager
from minijax.prompts import generate_text_completion_prompt

from ..utils import parse_generated_commands, execute_generated_commands


cfg = Config()


def gpt3_value_generator(zero_shot=True):
    def __wrapped(form):
        api_manager = ApiManager()
        
        form_html = form.get_attribute('outerHTML')
        prompt = generate_text_completion_prompt(form_html, zero_shot=zero_shot)
        response = api_manager.create_text_completion(
            prompt=prompt,
            model=cfg.model_config['parameters']['model'],
            temperature=cfg.model_config['parameters']['temperature'],
            # max_tokens=cfg.model_config['parameters']['max_tokens'],
        )
        
        response_text = response.choices[0].text
        commands = parse_generated_commands(response_text)
        
        return commands
    
    return __wrapped
