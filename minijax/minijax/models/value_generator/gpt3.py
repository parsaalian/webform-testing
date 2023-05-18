from __future__ import annotations

from minijax.config import Config
from minijax.llm.openai import ApiManager
from minijax.prompts import generate_text_completion_prompt

from ..utils import parse_generated_commands


cfg = Config()


def gpt3_value_generator(
    zero_shot: bool = True
) -> function:
    def __wrapped(
        form_prompt_str: str
    ) -> str:
        api_manager = ApiManager()
        
        prompt = generate_text_completion_prompt(form_prompt_str, zero_shot=zero_shot)
        response = api_manager.create_text_completion(
            prompt=prompt,
            model=cfg.model_config['parameters']['model'],
            temperature=cfg.model_config['parameters']['temperature'],
            # max_tokens=cfg.model_config['parameters']['max_tokens'],
        )
        
        response_text = response.choices[0].text
        
        return response_text
    
    return __wrapped
