import re
from .factory import ConstraintFactory


def split_functions(function_string):
    functions = []
    bracket_count = 0
    current_func = []
    for char in function_string:
        if char == '(':
            bracket_count += 1
        if char == ')':
            bracket_count -= 1
        if char == '.' and bracket_count == 0:
            functions.append(''.join(current_func).strip())
            current_func = []
        else:
            current_func.append(char)
    functions.append(''.join(current_func).strip())  # add the last function
    return functions


def generate_constraints_from_string(constraint_string):
    idx = 0
    splitted = split_functions(constraint_string)
    splitted = list(map(lambda x: x.strip(), splitted))
    transformed_constraints = []
    while idx < len(splitted):
        if splitted[idx] != 'not':
            transformed_constraints.append(splitted[idx])
            idx += 1
            continue
        transformed_constraints.append('not.' + splitted[idx + 1])
        idx += 2
    
    field_name = transformed_constraints[0].replace('expect(field(\'', '').replace('\'))', '')
    constraints = list(map(
        ConstraintFactory.create,
        transformed_constraints[1:]
    ))
    return field_name, constraints