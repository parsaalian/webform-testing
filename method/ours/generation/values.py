import openai

from method.llm.openai import ApiManager
from method.ours.prompts import (
    get_form_context,
    create_value_generation_user_prompt,
    value_generation_system_prompt
)
from method.ours.constraints import split_constant_and_field_constraints
from method.ours.feedback import get_local_feedback

from .utils import combine_contexts


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


def generate_value_for_input_group(
    input_group,
    value_table,
    context,
    global_feedback=[],
    ablation_inclusion={
        'relevant': True,
        'context': True,
        'date': True,
        'constraints': True,
        'feedback': True
    }
):
    value_entry = value_table.get_entry_by_input_group(input_group)
    
    constraints = value_entry.constraints
    constant_constraints, field_constraints = split_constant_and_field_constraints(constraints)
    including_constraints = [*constant_constraints]
    
    last_entry = value_table.get_entry_by_input_group(input_group)
        
    local_feedback = get_local_feedback(input_group)
    
    feedback_string = '\n'.join([*local_feedback, *global_feedback]).strip()
    
    last_try = {
        "value": last_entry.value,
        "feedback": feedback_string
    } if last_entry is not None and feedback_string != '' else None
    
    constraints = last_entry.constraints if last_entry is not None else None
    
    relevant_field_values = []
    for field_constraint in field_constraints:
        field_arg = field_constraint.get_field_args()[0]
        
        if field_arg not in value_table.entries:
            continue
        
        value = value_table.get_entry_by_field_id(field_arg).value
        
        if value is not None:
            including_constraints.append(field_constraint)
            relevant_field_values.append((field_arg, value))
    
    value_user_prompt = create_value_generation_user_prompt(
        context,
        value_entry.input_group,
        including_constraints,
        last_try=last_try,
        relevant_field_values=relevant_field_values if len(relevant_field_values) > 0 else None,
        ablation_inclusion=ablation_inclusion
    )
    
    generated_value = generate_values_with_llm(
        value_user_prompt,
        openai_api_key=openai.api_key
    )
    
    value_entry.set_value(generated_value)
    
    return value_table


def generate_values_for_input_groups(
    input_groups,
    value_table,
    global_feedback=[],
    app_context="",
    ablation_inclusion={
        'relevant': True,
        'context': True,
        'date': True,
        'constraints': True,
        'feedback': True
    }
):
    form_context = get_form_context(input_groups)
    context = combine_contexts(app_context, form_context)

    for input_group in input_groups:
        # skip submit button
        if input_group.node.element.name == 'button':
            continue
        
        value_entry = value_table.get_entry_by_input_group(input_group)
        
        if value_entry is None:
            continue
        
        value_table = generate_value_for_input_group(
            input_group,
            value_table,
            global_feedback=global_feedback,
            context=context,
            ablation_inclusion=ablation_inclusion
        )
    
    return value_table