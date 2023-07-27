import openai

from method.llm.openai import ApiManager
from method.ours.prompts import (
    get_form_context,
    constraint_generation_system_prompt,
    create_constraint_generation_user_prompt,
)
from method.ours.constraints import generate_constraints_from_string
from method.ours.feedback import get_local_feedback

from .utils import ValueTable


def generate_constraints_with_llm(
    user_constraint_prompt,
    openai_api_key,
    model='gpt-4',
    temperature=0,
    max_tokens=None,
):
    api_manager = ApiManager()
    
    messages = [
        {
            "role": "system",
            "content": constraint_generation_system_prompt,
        },
        {
            "role": "user",
            "content": user_constraint_prompt
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


def generate_constraints_for_input_group(
    input_group,
    value_table,
    form_context,
    global_feedback=[],
    ablation_inclusion={
        'context': True,
        'relevant': True,
        'constraints': True,
        'feedback': True,
    }
):
    last_entry = value_table.get_entry_by_input_group(input_group)
        
    local_feedback = get_local_feedback(input_group)
    
    feedback_string = '\n'.join([*local_feedback, *global_feedback]).strip()
    
    last_try = {
        "value": last_entry.value,
        "feedback": feedback_string
    } if last_entry is not None else None
    
    constraints = last_entry.constraints if last_entry is not None else None
    
    if last_try is None or (last_try is not None and feedback_string != ''):
        constraint_user_prompt = create_constraint_generation_user_prompt(
            form_context,
            input_group,
            last_try=last_try,
            constraints=constraints,
            ablation_inclusion=ablation_inclusion
        )
        
        generated_constraints = generate_constraints_with_llm(
            constraint_user_prompt,
            openai_api_key=openai.api_key
        )
        
        field_name, constraints = generate_constraints_from_string(generated_constraints)
        value_table.add_entry(field_name, input_group, constraints)
    
    return value_table


def generate_constraints_for_input_groups(
    input_groups,
    value_table=None,
    global_feedback=[],
    ablation_inclusion={
        'context': True,
        'relevant': True,
        'constraints': True,
        'feedback': True,
    }
):
    form_context = get_form_context(input_groups)
    
    if value_table is None:
        value_table = ValueTable()
    
    for input_group in input_groups:
        # skip submit button
        if input_group.node.element.name == 'button':
            continue
        
        try:
            value_table = generate_constraints_for_input_group(
                input_group,
                value_table,
                form_context,
                global_feedback=global_feedback,
                ablation_inclusion=ablation_inclusion
            )
        except Exception as e:
            print(e)
    
    return value_table