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


def get_form_context(input_groups):
    labels = list(filter(lambda x: x is not None, map(lambda x: x.label, input_groups)))
    return '\n'.join(map(lambda x: x.element.text, labels))


def create_constraint_generation_user_prompt(
    form_context,
    input_group,
    relevant_count=3,
    last_try=None,
    generated_constraint_string=None,
):
    constraint_generation_user_prompt = f'''
    The labels for the form are:
    {form_context}
    These labels are used to provide context for the functionality of the form.
    
    We are generating constraints for the following input field:
    {create_field_info_text(input_group)}
    
    The relevant information available in the form are (in order of relevance):
    {create_relevant_info_text(input_group, relevant_count)}
    
    {"The previously generated constraints are:" if generated_constraint_string is not None else ""}
    {generated_constraint_string if generated_constraint_string is not None else ""}
    
    {"We have tried to generate constraints for this field before." if last_try is not None else ""}
    {last_try["value"] if last_try is not None else ""}
    {"And got the following inline and global feedback:" if last_try is not None else ""}
    {last_try["feedback"] if last_try is not None else ""}
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