from __future__ import annotations

from minijax.config import Config
from minijax.llm.openai import ApiManager
from minijax.prompts import generate_parse_chat_completion_prompt


cfg = Config()


def chat_gpt_form_parser(
    zero_shot: bool = True
) -> function:
    def __wrapped(
        form_prompt_str: str
    ) -> str:
        api_manager = ApiManager()
        
        prompt = generate_parse_chat_completion_prompt(form_prompt_str)
        response = api_manager.create_chat_completion(
            messages=prompt,
            model=cfg.model_config['parameters']['model'],
            temperature=cfg.model_config['parameters']['temperature'],
            # max_tokens=cfg.model_config['parameters']['max_tokens'],
        )
        
        response_text = response.choices[0].message.content
        
        return response_text
    
    return __wrapped