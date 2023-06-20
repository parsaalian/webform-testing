from abc import ABC, abstractmethod

from .args import FieldArg


class Constraint(ABC):
    def __init__(self, is_negative, args=None):
        self.is_negative = is_negative
        self.args = args
        self.is_field = self._set_is_field(args)
    
    
    def _set_is_field(self, args):
        if args is None:
            return False
        for arg in args:
            if isinstance(arg, FieldArg):
                return True
        return False

    
    def get_field_args(self):
        return [arg.value for arg in self.args if isinstance(arg, FieldArg)]
    
    
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