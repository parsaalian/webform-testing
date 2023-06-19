def create_constraint_generation_prompt(
    input_group,
    relevant_count=3
):
    input_data_str = str(input_group)

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

    constraints_prompt = f'''
    {input_data_str}

    The relevant information available in the form are (in order of relevance):
    {relevant_input_groups_str}
    '''
    
    return constraints_prompt.strip()