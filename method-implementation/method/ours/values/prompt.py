from method.ours.constraints import create_constraint_generation_prompt


def create_value_generation_prompt(
    input_group,
    generated_constraints,
    relevant_count=3,
):
    # TODO: We will generate the values one-by-one from top to bottom.
    # for each value, if we have any relevant field and we have already
    # generated the value for that field, we will use that value if the
    # prompt. If not, we will not mention the relation or the value in
    # the prompt.
    
    constraints_prompt = create_constraint_generation_prompt(
        input_group, relevant_count=relevant_count
    )
    
    input_constraints_string = '\n'.join(map(lambda x: x.to_prompt_string(), generated_constraints))
    
    value_generation_prompt = f'''
    {constraints_prompt}

    generate values based on the following constraints:
    {input_constraints_string}
    '''.strip()
    
    return value_generation_prompt
