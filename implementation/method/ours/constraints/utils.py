from .factory import ConstraintFactory


def generate_constraints_from_string(constraint_string):
    field_name = constraint_string.split('\n.')[0].replace('expect(field(\'', '').replace('\'))', '')
    constraints = list(map(
        ConstraintFactory.create,
        constraint_string.split('\n.')[1:]
    ))
    return field_name, constraints