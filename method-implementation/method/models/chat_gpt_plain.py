from __future__ import annotations

from method.llm.openai import ApiManager


CHAT_COMPLETION_FILL_PROMPT_TEMPLATE = """
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

You can issue these commands:
    - FILL----X----"Y": Fill the <input> or <textarea> element that has a relative xpath X with value Y
    - SELECT----X----"Y": Select the option Y in the <select> element that has a relative xpath X
    - CLICK----X: Click on the element that has a relative xpath X, which is a checkbox or radio button
    - BLANK----X: Leave the element that has a relative xpath X blank (do nothing)

The xpath in this format must be relative to the form element. Just give the commands and nothing else.
"""


def chat_gpt_plain(form_html, model='gpt3.5-turbo'):
    api_manager = ApiManager()
    
    prompt = [
        {
            "role": "system",
            "content": CHAT_COMPLETION_FILL_PROMPT_TEMPLATE,
        },
        {
            "role": "user",
            "content": """
            The form HTML is:
            {form_html}
            Parse this form in the specified format. Don't explain your process, just give the JSON output. Make sure your output can be parsed by json.loads.
            """.format(form_html=form_html)
        }
    ]
    
    response = api_manager.create_chat_completion(
        prompt=prompt,
        model=model,
        temperature=0.0,
        max_tokens=256,
    )
    
    response_text = response.choices[0].text()
    
    return response_text