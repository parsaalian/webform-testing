import json
import copy
from abc import ABC, abstractmethod


class ActionBase(ABC):
    def __init__(self, xpath, parent_state, execution_count=1):
        self.xpath = xpath
        self.parent_state = parent_state
        self.execution_count = execution_count
        self.outer_domain = False
        
        # execution result is determined by the state while executing action
        self.execution_data = None
        # action data is determined by action while getting executed
        self.action_data = {}
        # this is a combination of the two above
        self.execution_result = None
    
    
    def get_execution_count(self):
        return self.execution_count
    
    
    def get_xpath(self):
        return self.xpath
    
    
    def set_execution_result(self, execution_data):
        success, exception = execution_data
        self.execution_result = ExecutionResult(success, exception, self.action_data)
    
    
    def copy(self):
        return copy.copy(self)
    
    
    @abstractmethod
    def execute(self):
        '''executes the action'''
        pass
    
    
    @abstractmethod
    def retry(self):
        '''re-executes the action'''
        pass
    
    
    @abstractmethod
    def id(self):
        '''returns a unique id for the action'''
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
    
    
    def __str__(self):
        return f"{json.dumps(self.to_json())}"