from method.llm.openai import ApiManager


# number of tokens: 129
value_generation_prompt = """
Your task is to generate a set of values for a form field based on the form field information and a set of constraints on the field. Your decisions must always be made independently without seeking user assistance or additional information.
For each user prompt, you need to generate five distinct values that satisfy the constraints while keeping in mind the nature of the input from the available information.
Only generate the values and don't explain your answers.
Generate the values in a Python array. We must be able to parse your generation with json.loads.
Only generate values for the inputs in question, and not the ones in the relevant information section.
""".strip()


def generate_values_with_llm(
    user_value_prompt,
    openai_api_key,
    model='gpt-4',
    temperature=0,
    max_tokens=None,
):
    api_manager = ApiManager()
    
    messages = [
        {
            "role": "system",
            "content": value_generation_prompt,
        },
        {
            "role": "user",
            "content": f"""
            We are generating values for the following input field:
            {user_value_prompt}
            """.strip()
        }
    ]
    
    response = api_manager.create_chat_completion(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        openai_api_key=openai_api_key
    )
    
    response_text = response.choices[0].message.content
    
    return response_text
