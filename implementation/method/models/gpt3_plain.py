from __future__ import annotations

from method.config import Config
from method.llm.openai import ApiManager
from method.prompts import generate_parse_text_completion_prompt

TEXT_COMPLETION_FILL_PROMPT_ZERO_SHOT_TEMPLATE = """You are an agent filling forms on a website. You can issue these commands:
    - FILL----X----"Y": Fill the <input> or <textarea> element that has a relative xpath X with value Y
    - SELECT----X----"Y": Select the option Y in the <select> element that has a relative xpath X
    - CLICK----X: Click on the element that has a relative xpath X, which is a checkbox or radio button
    - BLANK----X: Leave the element that has a relative xpath X blank (do nothing)
Each command must be issued in a new line, with no preceding or trailing text values.
You are given a form to fill. The form's html is as follows:
{form_html}
The xpath in this format must be relative to the form element. Just give the commands and nothing else.
YOUR COMMANDS:"""

cfg = Config()

def gpt3_form_parser(
    zero_shot: bool = True
) -> function:
    def _wrapped(
        form_prompt_str: str
    ) -> str:
        api_manager = ApiManager()
        
        prompt = generate_parse_text_completion_prompt(form_prompt_str, zero_shot=zero_shot)
        response = api_manager.create_text_completion(
            prompt=prompt,
            model=cfg.model_config['parameters']['model'],
            temperature=cfg.model_config['parameters']['temperature'],
            max_tokens=cfg.model_config['parameters']['max_tokens'],
        )
        
        response_text = response.choices[0].text
        
        return response_text

    return _wrapped