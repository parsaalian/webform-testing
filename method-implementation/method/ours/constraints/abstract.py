from abc import ABC, abstractmethod


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