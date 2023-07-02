from .utils import generate_constraints_from_string


def split_constant_and_field_constraints(constraints):
    constants = list(filter(lambda x: not x.is_field, constraints))
    fields = list(filter(lambda x: x.is_field, constraints))
    return constants, fields


__all__ = [
    'split_constant_and_field_constraints',
    'generate_constraints_from_string',
]