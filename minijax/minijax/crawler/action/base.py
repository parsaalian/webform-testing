from abc import ABC, abstractmethod


class ActionBase(ABC):
    def __init__(self, action_element_xpath, execution_count=1):
        self.xpath = action_element_xpath
        self.execution_count = execution_count
        self.last_execution_data = {}
        self.execution_history = []
    
    
    def get_execution_count(self):
        return self.execution_count
    
    
    def get_xpath(self):
        return self.xpath
    
    
    def add_history_entry(self, result):
        result.data = self.last_execution_data
        self.execution_history.append(result)
    
    
    @abstractmethod
    def execute(self):
        '''executes the action'''
        pass
    
    
    def __str__(self):
        return f"Action {type(self)} at XPATH: {self.xpath}"

    
    def __eq__(self, other):
        return type(self) == type(other) and self.xpath == other.xpath


class ExecutionResult:
    def __init__(self, success=False, exception=None, data={}):
        self.success = success
        self.exception = exception
        self.data = data
    
    
    def to_json(self):
        return {
            'success': self.success,
            'exception': self.exception,
            'data': self.data
        }