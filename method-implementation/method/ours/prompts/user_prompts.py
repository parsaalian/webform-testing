def format_extra_tabs(input_str):
    return input_str.replace('\n\t\t', '\n').replace('\n\t', '\n')


def create_field_info_text(input_group):
    input_data_str = str(input_group)
    
    return input_data_str.strip()


def create_relevant_info_text(input_group, relevant_count=3):
    relevant_input_groups = list(map(
        lambda x: str(x[0]).split('with the following relevant text tags')[0],
        sorted(input_group.edges, key=lambda x: x[1], reverse=True)
    ))
    
    relevant_input_groups_str = "\n".join(
        map(
            lambda data: f'''{data[0] + 1}.\n{data[1]}'''.strip(),
            enumerate(relevant_input_groups[:relevant_count])
        )
    )
    
    return relevant_input_groups_str.strip()


def create_constraint_generation_user_prompt(
    input_group,
    relevant_count=3,
    last_try=None,
    generated_constraint_string=None,
):
    constraint_generation_user_prompt = f'''
    We are generating constraints for the following input field:
    {create_field_info_text(input_group)}
    The relevant information available in the form are (in order of relevance):
    {create_relevant_info_text(input_group, relevant_count)}
    '''.strip()
    
    if generated_constraint_string is not None:
        constraint_generation_user_prompt = f'''
        {constraint_generation_user_prompt}
        The previously generated constraints are:
        {generated_constraint_string}
        '''.strip()
    
    if last_try is not None:
        constraint_generation_user_prompt = f'''
        {constraint_generation_user_prompt}
        We have tried the following value:
        {last_try['value']}
        And got the following feedback:
        {last_try['feedback']}
        '''.strip()
    
    return format_extra_tabs(constraint_generation_user_prompt)


def create_constraints_text(constraints):
    input_constraints_string = '\n'.join(map(lambda x: x.to_prompt_string(), constraints))
    return input_constraints_string


def create_relevant_field_values_text(relevant_field_values):
    relevant_field_values_string = '\n'.join(map(lambda x: f'field: {x[0]}, value: {x[1]}', relevant_field_values))
    return relevant_field_values_string


def create_value_generation_user_prompt(
    input_group,
    constraints,
    relevant_count=3,
    relevant_field_values=None,
):
    value_generation_user_prompt = f'''
    We are generating filling values for the following input field:
    {create_field_info_text(input_group)}
    The relevant information available in the form are (in order of relevance):
    {create_relevant_info_text(input_group, relevant_count)}
    The constraints on this input field are:
    {create_constraints_text(constraints)}
    '''.strip()
    
    if relevant_field_values is not None:
        value_generation_user_prompt = f'''
        {value_generation_user_prompt}
        The values for the fields in constraints are:
        {relevant_field_values}
        '''.strip()
    
    return format_extra_tabs(value_generation_user_prompt)