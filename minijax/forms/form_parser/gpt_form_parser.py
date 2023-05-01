import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt3_parse_form(form):
    form_html = form.get_attribute('outerHTML')
    
    parse_prompt = f'''Parse the following forms into a JSON object:
    HTML:
    <form>
        <label for="fname">First name:</label>
        <input type="text" id="fname" name="fname" />
        
        <label for="lname">Last name:</label>
        <input type="text" id="lname" name="lname" />
    </form>
    JSON:
    [
        {{
            "label": "First Name:",
            "tag": "input",
            "attributes": {{
                "type": "text",
                "id": "fname",
                "name": "fname"
            }}
        }},
        {{
            "label": "Last Name:",
            "tag": "input",
            "attributes": {{
                "type": "text",
                "id": "lname",
                "name": "lname",
            }}
        }}
    ]
    ========
    HTML:
    {form_html}
    JSON:
    '''
    
    print(parse_prompt)
    
    parse_res = openai.Completion.create(
        model="text-davinci-003",
        prompt=parse_prompt,
        temperature=0,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        max_tokens=1024,
    )
    
    return parse_res.choices[0].text.strip()


def chat_gpt_parse_form(form, model):
    form_html = form.get_attribute('outerHTML')
    
    parse_prompt = f'''We want to parse inputs of an HTML form in the following format:
    HTML:
    <form>
        <label for="fname">First name:</label>
        <input type="text" id="fname" name="fname" />
        
        <label for="lname">Last name:</label>
        <input type="text" id="lname" name="lname" />
    </form>
    JSON:
    [
        {{
            "label": "First Name:",
            "tag": "input",
            "attributes": {{
                "type": "text",
                "id": "fname",
                "name": "fname"
            }}
        }},
        {{
            "label": "Last Name:",
            "tag": "input",
            "attributes": {{
                "type": "text",
                "id": "lname",
                "name": "lname",
            }}
        }}
    ]

    Parse the following form:
    {form_html}

    Just include the inputs, text areas, buttons, etc. Also, have the xpath in attributes.
    '''

    print(parse_prompt)
    
    parse_res = openai.ChatCompletion.create(
        model=model,
        messages=[
                {"role": "user", "content": parse_prompt},
            ]
    )
    
    return parse_res.choices[0].message.content.strip()


def gpt35_parse_form(form):
    return chat_gpt_parse_form(form, "gpt-3.5-turbo")


def gpt4_parse_form(form):
    return chat_gpt_parse_form(form, "gpt-4")