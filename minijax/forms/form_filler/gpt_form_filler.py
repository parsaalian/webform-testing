import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt3_fill_form_plain(form):
    form_html = form.get_attribute('outerHTML')
    
    fill_prompt = f'''Generate values for the following forms:
    HTML:
    <form>
        <label for="fname">First name:</label>
        <input type="text" id="fname" name="fname" xpath="a" />
        
        <label for="lname">Last name:</label>
        <input type="text" id="lname" name="lname" xpath="b" />
    </form>
    Values:
    [
        {{
            "xpath": "a",
            "value": "John",
        }},
        {{
            "xpath": "b",
            "value": "Doe",
        }}
    ]
    ========
    HTML:
    {form_html}
    JSON:
    '''
    
    print(fill_prompt)
    
    parse_res = openai.Completion.create(
        model="text-davinci-003",
        prompt=fill_prompt,
        temperature=0,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        max_tokens=1024,
    )
    
    return parse_res.choices[0].text.strip()


def chat_gpt_fill_form_plain(form, model):
    form_html = form.get_attribute('outerHTML')
    
    fill_prompt = f'''We want to fill inputs of an HTML form in the following format:
    HTML:
    <form>
        <label for="fname">First name:</label>
        <input type="text" id="fname" name="fname" xpath="a" />
        
        <label for="lname">Last name:</label>
        <input type="text" id="lname" name="lname" xpath="b" />
    </form>
    Values:
    [
        {{
            "xpath": "a",
            "value": "John",
        }},
        {{
            "xpath": "b",
            "value": "Doe",
        }}
    ]
    
    Generate values for the following form:
    {form_html}
    Include all the input types in your json object.
    '''
    
    print(fill_prompt)
    
    fill_res = openai.ChatCompletion.create(
        model=model,
        messages=[
                {"role": "user", "content": fill_prompt},
            ]
    )
    
    return fill_res.choices[0].message.content.strip()


def gpt35_fill_form_plain(form):
    return chat_gpt_fill_form_plain(form, "gpt-3.5-turbo")


def gpt4_fill_form_plain(form):
    return chat_gpt_fill_form_plain(form, "gpt-4")