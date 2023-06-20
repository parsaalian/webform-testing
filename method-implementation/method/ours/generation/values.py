from method.llm.openai import ApiManager
from method.ours.prompts import value_generation_system_prompt


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
            "content": value_generation_system_prompt,
        },
        {
            "role": "user",
            "content": user_value_prompt
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
