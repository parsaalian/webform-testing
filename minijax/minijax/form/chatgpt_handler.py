import json
import openai

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from minijax.config import Config


cfg = Config()


system_prompt = '''
You are FormGPT, an AI assistant embedded in a crawler that has the task of generating different values for form inputs.
Your decisions must always be made independently without seeking user assistance. Play to your strengths as an LLM and pursue simple strategies.

GOALS:
1. Given a form HTML, understand the purpose of the form, and generate values for each input in the form.

CONSTRAINTS:
1. No user assistance

Performance Evaluation:
1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.
2. Constructively self-criticize your big-picture behavior constantly.
3. Reflect on past decisions and strategies to refine your approach.
4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.
Write all code to a file.

You can issue these commands:
    - FILL----X----"Y": Fill the <input> or <textarea> element that has a relative xpath X with value Y
    - SELECT----X----"Y": Select the option Y in the <select> element that has a relative xpath X

The xpath in this format must be relative to the form element. Ensure the response can be parsed by Python json.loads.
'''


def fill_form_chatgpt(form, model='gpt-3.5-turbo', zero_shot=True):
    form_html = form.get_attribute('outerHTML')
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": f"""
            The form HTML is:
            {form_html}
            Determine which next command to use, and respond using the format specified above:
            """
        }
    ]
    res = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    print(res.choices[0].message.content)
    commands = res.choices[0].message.content.split('\n')
    print(commands)
    values = {}
    for command in commands:
        print(command)
        cmd, xpath, value = command.split('----')
        value = value.strip('"')
        values[xpath] = value
        if cmd == 'FILL':
            form.find_element(By.XPATH, xpath).send_keys(value)
    return values