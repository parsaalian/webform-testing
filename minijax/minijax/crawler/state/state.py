import time
import hashlib
from urllib.parse import urlparse

from selenium.webdriver.common.by import By

from minijax.config import Config
from minijax.logger import logger
from minijax.crawler import get_driver_container
from minijax.crawler.action import (
    ExecutionResult,
    GoToRootAction,
    find_click_actions,
    find_form_actions,
    find_hover_actions,
)


cfg = Config()


class State:
    def __init__(self, url, html, text, prev_state, prev_action):
        self.driver = get_driver_container().get_driver()
        self.url = url
        self.html = html
        self.text = text
        self.root_path = []
        self.actions = []
        # value of neighbors is never used for now
        self.neighbors = {}
        
        self._eval_root_path(prev_state, prev_action)
        self._eval_actions()
    
    
    def _eval_root_path(self, prev_state, prev_action):
        if prev_state is None:
            self.root_path = [GoToRootAction()]
        else:
            self.root_path = [*prev_state.root_path]
            self.root_path.append(prev_action)
    
    
    def _eval_actions(self):
        actions = []
        
        click_actions = find_click_actions(self.driver)
        hover_actions = find_hover_actions(self.driver)
        form_actions = find_form_actions(self.driver)
        
        if cfg.crawler_config['action']['enabled']['click']:
            actions = [*actions, *click_actions]
        if cfg.crawler_config['action']['enabled']['hover']:
            actions = [*actions, *hover_actions]
        if cfg.crawler_config['action']['enabled']['form']:
            actions = [*actions, *form_actions]
        
        self.actions = actions
    
    
    def _add_neighbor(self, action, neighbor_state):
        self.neighbors[action.id()] = neighbor_state
    
    
    def get_to_state(self):
        for action in self.root_path:
            action.execute()
            time.sleep(cfg.crawler_config['wait']['after_action'])
    
    
    def get_neighbors(self):
        return self.neighbors
    
    
    def execute_actions(self, actions_to_exclude=[]):
        # create a queue with the number of times that we tried to execute an action
        # some actions (like form filling) might have multiple executions
        action_execution_queue = []
        for action in self.actions:
            execution_count = action.get_execution_count()
            for _ in range(execution_count):
                action_execution_queue.append((action.copy(), 0))
        
        while len(action_execution_queue) > 0:
            action, retries = action_execution_queue.pop(0)
            
            # might cause problems in an SPA application where URL won't change but content will
            if action.xpath in actions_to_exclude and cfg.crawler_config['action']['should_exclude_duplicates']:
                logger.debug(f'Skipping: {action}')
                continue
            
            if action.outer_domain:
                logger.debug(f'Skipping: {action} (outer domain)')
                continue
            
            try:
                logger.debug(f'Executing: {action}')
                action.execute()
                
                action.set_execution_result((True, None))
                
                time.sleep(cfg.crawler_config['wait']['after_action'])

            except Exception as e:
                logger.debug(f'Exception: {e}')
                
                action.set_execution_result((False, str(e)))
                
                if retries + 1 < cfg.crawler_config['action']['max_retries_after_fail']:
                    action_execution_queue.append((action, retries + 1))
                    logger.debug(f'{action} failed {retries + 1} times. Retrying Later.')
                else:
                    logger.debug(f'{action} failed {retries + 1} times. Skipping.')
            
            # check if action leads to invalid domain
            current_state_domain = urlparse(self.url, scheme='', allow_fragments=True).netloc
            new_state_domain = urlparse(self.driver.current_url, scheme='', allow_fragments=True).netloc
            if current_state_domain != new_state_domain:
                logger.info('Action leads to invalid domain')
                action.outer_domain = True
            
            else:
                body = self.driver.find_element(By.TAG_NAME, 'body')
                new_state = State(
                    self.driver.current_url,
                    body.get_attribute('outerHTML'),
                    body.text,
                    self,
                    action
                )
                
                if self != new_state:
                    self._add_neighbor(action, new_state)
                
            self.get_to_state()
    
    
    def to_json(self):
        return {
            'id': self.id(),
            'url': self.url,
            'html': self.html,
            'text': self.text,
            'root_path': [str(action) for action in self.root_path],
            'actions': [str(action) for action in self.actions],
            'neighbors': {
                action: state.id() for action, state in self.neighbors.items()
            }
        }
    
    
    def id(self):
        return hashlib.md5(str(self).encode('utf-8')).hexdigest()
    
    
    def __str__(self):
        action_str = '\n'.join([str(action) for action in self.actions])
        return f"""
            State: {self.url}
            Actions:
            {action_str}
        """
    
    
    def __eq__(self, other):
        if type(other) != State:
            return False
        
        # representation-based comparison, might have faults
        if str(self) != str(other):
            return False
        
        # text-based comparison: maybe pages have the same actions but content is different
        if self.text != other.text:
            return False
        
        # full attributes comparison
        '''if self.url != other.url:
            return False
        if len(self.actions) != len(other.actions):
            return False
        for action in self.actions:
            if action not in other.actions:
                return False
        for action in other.actions:
            if action not in self.actions:
                return False'''
        
        return True
