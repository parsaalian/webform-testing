import re
from .factory import ConstraintFactory


def generate_constraints_from_string(constraint_string):
    idx = 0
    splitted = re.split('\n\.|\.', constraint_string)
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