from minijax.prompts.templates import (
    TEXT_COMPLETION_PARSE_PROMPT_ZERO_SHOT_TEMPLATE,
    TEXT_COMPLETION_PARSE_PROMPT_FEW_SHOT_TEMPLATE,
    TEXT_COMPLETION_FILL_PROMPT_ZERO_SHOT_TEMPLATE,
    TEXT_COMPLETION_FILL_PROMPT_FEW_SHOT_TEMPLATE,
    CHAT_COMPLETION_FILL_PROMPT_TEMPLATE,
)


def generate_parse_text_completion_prompt(form_html, zero_shot=True):
    if zero_shot:
        return TEXT_COMPLETION_PARSE_PROMPT_ZERO_SHOT_TEMPLATE.format(form_html=form_html)
    return TEXT_COMPLETION_PARSE_PROMPT_FEW_SHOT_TEMPLATE.format(form_html=form_html)


def generate_parse_chat_completion_prompt(form_html):
    return [
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


def generate_fill_text_completion_prompt(form_html, zero_shot=True):
    if zero_shot:
        return TEXT_COMPLETION_FILL_PROMPT_ZERO_SHOT_TEMPLATE.format(form_html=form_html)
    return TEXT_COMPLETION_FILL_PROMPT_FEW_SHOT_TEMPLATE.format(form_html=form_html)


def generate_fill_chat_completion_prompt(form_html):
    return [
        {
            "role": "system",
            "content": CHAT_COMPLETION_FILL_PROMPT_TEMPLATE,
        },
        {
            "role": "user",
            "content": """
            The form HTML is:
            {form_html}
            Determine which next command to use, and respond using the format specified above:
            """.format(form_html=form_html)
        }
    ]
