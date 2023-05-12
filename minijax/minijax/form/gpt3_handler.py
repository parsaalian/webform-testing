import openai
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from minijax.config import Config


cfg = Config()


gpt3_completion_prompt = """You are an agent filling forms on a website. You can issue these commands:
    - FILL////X////"Y": Fill the <input> or <textarea> element that has a relative xpath X with value Y
    - SELECT////X////"Y": Select the option Y in the <select> element that has a relative xpath X
Each command must be issued in a new line, with no preceding or trailing text values.
You are given a form to fill. The form's html is as follows:
{form_html}
The xpath in this format must be relative to the form element. Just give me the commands and nothing else.
YOUR COMMANDS:"""


def fill_form_gpt3(form, zero_shot=True):
    form_html = form.get_attribute('outerHTML')
    prompt = gpt3_completion_prompt.format(form_html=form_html)
    res = openai.Completion.create(
        model=cfg.llm_config['parameters']['model'],
        prompt=prompt,
        temperature=cfg.llm_config['parameters']['temperature'],
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    values = {}
    commands = res.choices[0].text.split('\n')[1:]
    print(commands)
    for command in commands:
        try:
            print(command)
            cmd, xpath, value = command.split('////')
            values[xpath] = value
            if cmd == 'FILL':
                form.find_element(By.XPATH, xpath).send_keys(value)
            elif cmd == 'SELECT':
                select = Select(form.find_element(By.XPATH, xpath))
                select.select_by_visible_text(value)
        except:
            continue
    return values