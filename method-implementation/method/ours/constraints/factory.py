from abc import ABC, abstractmethod


class ConstraintFactory:
    @staticmethod
    def create(constraint_string):
        is_negative = constraint_string.startswith('not.')
        rest = list(filter(lambda x: x != '', constraint_string.split('not.')))[0]
        name = rest.split('(')[0]
        args = list(filter(
            lambda x: x != '',
            map(
                lambda x: x.strip(),
                rest.replace(name, '')[1:-1].split(',')
            )
        ))
        
        args = list(map(ConstraintFactory._map_arg_to_object, args))
        
        constraint_object = ConstraintFactory._create_object_from_parse_result(name, is_negative, args)
        
        return constraint_object
    
    
    @staticmethod
    def _map_arg_to_object(arg):
        if arg.startswith('field(\''):
            return FieldArg(arg.replace('field(\'', '').replace('\')', ''))
        return ConstantArg(arg)
    
    
    @staticmethod
    def _create_object_from_parse_result(name, is_negative, args):
        if name == 'toBe':
            return ToBe(is_negative, args)
        if name == 'toBeTruthy':
            return ToBeTruthy(is_negative)
        if name == 'toHaveLengthCondition':
            return ToHaveLengthCondition(is_negative, args)
        if name == 'toHaveCompareCondition':
            return ToHaveCompareCondition(is_negative, args)
        if name == 'toContainSubstr':
            return ToContainSubStr(is_negative, args)
        if name == 'toContainChar':
            return ToContainChar(is_negative, args)
        if name == 'toBeAlpha':
            return ToBeAlpha(is_negative)
        if name == 'toBeNumeric':
            return ToBeNumeric(is_negative)
        if name == 'toBeAlphaNumeric':
            return ToBeAlphaNumeric(is_negative)
        if name == 'toHaveUpperCase':
            return ToHaveUpperCase(is_negative)
        if name == 'toHaveSpecialChars':
            return ToHaveSpecialChars(is_negative)
        if name == 'toHaveWhiteSpace':
            return ToHaveWhiteSpace(is_negative)
        if name == 'toStartWith':
            return ToStartWith(is_negative, args)
        if name == 'toEndWith':
            return ToEndWith(is_negative, args)
        if name == 'toMatch':
            return ToMatch(is_negative, args)
        raise Exception('Constraint name is not valid')


class ConstantArg:
    def __init__(self, value):
        self.value = value
    
    
    def __str__(self):
        return str(self.value)


class FieldArg:
    def __init__(self, field_name):
        self.field_name = field_name
    
    
    def __str__(self):
        return f'field({self.field_name})'


class Constraint(ABC):
    def __init__(self, is_negative, args=None):
        self.is_negative = is_negative
        self.args = args
    
    
    @abstractmethod
    def to_prompt_string(self):
        pass
    
    
    @abstractmethod
    def has_conflict(self, other):
        '''
        In resolving conflicts, we assume that both constraints has been held at the same time.
        '''
        pass
    
    
    @abstractmethod
    def matches(self, value):
        pass


class ToBe(Constraint):
    def __init__(self, is_negative, args):
        super().__init__(is_negative, args)
        self.expected = args[0]
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not be {str(self.expected)}'
        return f'input field should be {str(self.expected)}'
    
    
    def has_conflict(self, other):
        if isinstance(other, ToBe):
            return (
                # if the expected values are different and both must be held
                self.expected != other.expected  and not self.is_negative and not other.is_negative
            ) or (
                # if the expected values are the same, but one is negative and the other is not
                self.expected == other.expected and self.is_negative != other.is_negative
            )
        if isinstance(other, ToBeTruthy):
            return (
                # if we expect empty value, but have value for this field
                other.is_negative and not not self.expected
            ) or (
                # if we expect non-empty value, but have empty value for this field
                not other.is_negative and not self.expected
            )
        if isinstance(other, ToHaveLengthCondition):
            return (
                not other.is_negative and not other.matches(self.expected)
            ) or (
                other.is_negative and other.matches(self.expected)
            )
        return False
    
    
    def matches(self, value):
        return value == self.expected


class ToBeTruthy(Constraint):
    def __init__(self, is_negative):
        super().__init__(is_negative)
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return 'input field should be empty'
        return 'input field should be non-empty'
    
    
    def has_conflict(self, other):
        if isinstance(other, ToBe):
            return other.has_conflict(self)
        if isinstance(other, ToBeTruthy):
            return self.is_negative != other.is_negative
        return False

    
    def matches(self, value):
        return False



class ToHaveLengthCondition(Constraint):
    def __init__(self, is_negative, args):
        super().__init__(is_negative, args)
        self.condition = args[0].strip("\'")
        self.length = args[1]
    
    
    def to_prompt_string(self):
        condition_string = ''
        if self.condition == '<':
            condition_string = 'less than' if not self.is_negative else 'greater than or equal to'
        if self.condition == '<=':
            condition_string = 'less than or equal to' if not self.is_negative else 'greater than'
        if self.condition == '>':
            condition_string = 'greater than' if not self.is_negative else 'less than or equal to'
        if self.condition == '>=':
            condition_string = 'greater than or equal to' if not self.is_negative else 'less than'
        if self.condition == '==':
            condition_string = 'equal to' if not self.is_negative else 'not equal to'
        if self.condition == '!=':
            condition_string = 'not equal to' if not self.is_negative else 'equal to'
        return f'input field should be {condition_string} {self.length} characters'
    
    
    def has_conflict(self, other):
        if isinstance(other, ToBe):
            return other.has_conflict(self)
        if isinstance(other, ToBeTruthy):
            return other.has_conflict(self)
        if isinstance(other, ToHaveLengthCondition):
            pass
        return False

    
    def matches(self, value):
        return False



class ToHaveCompareCondition(Constraint):
    def __init__(self, is_negative, args):
        super().__init__(is_negative, args)
        self.condition = args[0].strip("\'")
        self.expected = args[1]
    
    
    def to_prompt_string(self):
        condition_string = ''
        if self.condition == '<':
            condition_string = 'less than' if not self.is_negative else 'greater than or equal to'
        if self.condition == '<=':
            condition_string = 'less than or equal to' if not self.is_negative else 'greater than'
        if self.condition == '>':
            condition_string = 'greater than' if not self.is_negative else 'less than or equal to'
        if self.condition == '>=':
            condition_string = 'greater than or equal to' if not self.is_negative else 'less than'
        if self.condition == '==':
            condition_string = 'equal to' if not self.is_negative else 'not equal to'
        if self.condition == '!=':
            condition_string = 'not equal to' if not self.is_negative else 'equal to'
        return f'input field should be {condition_string} {str(self.expected)}'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToMatch(Constraint):
    def __init__(self, is_negative, args):
        super().__init__(is_negative, args)
        self.expected = args[0]
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not match {str(self.expected)} regex pattern'
        return f'input field should match {str(self.expected)} regex pattern'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToContainSubStr(Constraint):
    def __init__(self, is_negative, args):
        super().__init__(is_negative, args)
        self.expected = args[0]
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not contain {str(self.expected)} substring'
        return f'input field should contain {str(self.expected)} substring'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToContainChar(Constraint):
    def __init__(self, is_negative, args):
        super().__init__(is_negative, args)
        self.expected = args[0]
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not contain {str(self.expected)} character'
        return f'input field should contain {str(self.expected)} character'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToBeAlpha(Constraint):
    def __init__(self, is_negative):
        super().__init__(is_negative)
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return 'input field should not be alphabetic'
        return 'input field should be alphabetic'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToBeNumeric(Constraint):
    def __init__(self, is_negative):
        super().__init__(is_negative)
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return 'input field should not be numeric'
        return 'input field should be numeric'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToBeAlphaNumeric(Constraint):
    def __init__(self, is_negative):
        super().__init__(is_negative)
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return 'input field should not be alphanumeric'
        return 'input field should be alphanumeric'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToHaveUpperCase(Constraint):
    def __init__(self, is_negative):
        super().__init__(is_negative)
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not have uppercase characters'
        return f'input field should have uppercase characters'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToHaveSpecialChars(Constraint):
    def __init__(self, is_negative):
        super().__init__(is_negative)
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not have special characters'
        return f'input field should have special characters'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToHaveWhiteSpace(Constraint):
    def __init__(self, is_negative):
        super().__init__(is_negative)
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not have whitespace characters'
        return f'input field should have whitespace characters'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToStartWith(Constraint):
    def __init__(self, is_negative, args=None):
        super().__init__(is_negative, args)
        self.expected = args[0]
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not start with {str(self.expected)}'
        return f'input field should start with {str(self.expected)}'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToEndWith(Constraint):
    def __init__(self, is_negative, args=None):
        super().__init__(is_negative, args)
        self.expected = args[0]
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not end with {str(self.expected)}'
        return f'input field should end with {str(self.expected)}'
    
    
    def has_conflict(self, other):
        return False

    
    def matches(self, value):
        return False


class ToMatch(Constraint):
    def __init__(self, is_negative, args=None):
        super().__init__(is_negative, args)
        self.expected = args[0]
    
    
    def to_prompt_string(self):
        if self.is_negative:
            return f'input field should not match {str(self.expected)} regex pattern'
        return f'input field should match {str(self.expected)} regex pattern'
    
    
    def has_conflict(self, other):
        return False
    
    
    def matches(self, value):
        return False