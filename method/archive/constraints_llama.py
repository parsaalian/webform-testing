from method.ours.prompts import (
    get_form_context,
    constraint_generation_system_prompt,
    create_constraint_generation_user_prompt,
)
from method.ours.constraints import generate_constraints_from_string_llama
from method.ours.feedback import get_local_feedback

from method.ours.generation.utils import ValueTable, combine_contexts
import traceback

def generate_constraints_with_llama(
    model, 
    tokenizer, 
    user_constraint_prompt,
    temperature=0.0,
    max_tokens=512,
):    
    prompt_template = f'''[INST] <<SYS>>
    {constraint_generation_system_prompt}
    <</SYS>>

    {user_constraint_prompt}
    DO NOT EXPLAIN YOUR ANSWERS. [/INST]
    '''

    input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
    output = model.generate(inputs=input_ids, temperature=temperature, max_new_tokens=max_tokens)
    output_from_llm = tokenizer.decode(output[0])

    return output_from_llm


def generate_constraints_for_input_group_llama(
    model, 
    tokenizer, 
    input_group,
    value_table,
    context,
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
            context,
            input_group,
            last_try=last_try,
            constraints=constraints,
            ablation_inclusion=ablation_inclusion
        )
        
        generated_constraints = generate_constraints_with_llama(
            model, 
            tokenizer,
            constraint_user_prompt,            
        )
        
        print(generated_constraints)
        field_name, constraints = generate_constraints_from_string_llama(generated_constraints)
        value_table.add_entry(field_name, input_group, constraints)
    
    return value_table


def generate_constraints_for_input_groups_llama(
    model, 
    tokenizer,
    input_groups,
    value_table=None,
    global_feedback=[],
    app_context="",
    ablation_inclusion={
        'context': True,
        'relevant': True,
        'constraints': True,
        'feedback': True,
    }
):
    form_context = get_form_context(input_groups)
    context = combine_contexts(app_context, form_context)
    
    if value_table is None:
        value_table = ValueTable()
    
    for input_group in input_groups:
        #print(f"input_group:{input_group}")
        # skip submit button
        if input_group.node.element.name == 'button':
            continue
        
        try:
            value_table = generate_constraints_for_input_group_llama(
                model, 
                tokenizer,
                input_group,
                value_table,
                context,
                global_feedback=global_feedback,
                ablation_inclusion=ablation_inclusion
            )
        except Exception as e:
            print(str(e))
            print(e)
            traceback.print_exc()
    
    return value_table