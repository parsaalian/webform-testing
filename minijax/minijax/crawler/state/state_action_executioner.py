import time
from urllib.parse import urlparse

from selenium.webdriver.common.by import By

from minijax.config import Config
from minijax.logger import logger
from minijax.crawler import get_driver_container
from minijax.crawler.state.state import State


cfg = Config()
driver = get_driver_container().get_driver()


class StateActionExecutioner:
    def __init__(self):
        self.executed_action_map = {}
    
    
    def has_executed_action_in_url(self, url, action_id):
        if url not in self.executed_action_map:
            return False
        if action_id not in self.executed_action_map[url]:
            return False
        return True
    
    
    def add_executed_action_to_map(self, url, action_id, new_state):
        if url not in self.executed_action_map:
            self.executed_action_map[url] = {}
        if not self.has_executed_action_in_url(url, action_id):
            self.executed_action_map[url][action_id] = new_state
    
    
    def get_executed_actions_in_url(self, url):
        if url in self.executed_action_map:
            return self.executed_action_map[url]
        return {}
    
    
    def add_state_actions_to_map(self, state):
        for action_id, neighbor_state in state.get_neighbors().items():
            self.add_executed_action_to_map(state.url, action_id, neighbor_state)

    
    def get_actions_to_exclude(self, state):
        return self.get_executed_actions_in_url(state.url)
    
    
    def create_action_execution_queue(self, actions):
        # create a queue with the number of times that we tried to execute an action
        # some actions (like form filling) might have multiple executions
        action_execution_queue = []
        for action in actions:
            execution_count = action.get_execution_count()
            for _ in range(execution_count):
                action_execution_queue.append((action.copy(), 0))
        
        return action_execution_queue


    def should_exclude_action(self, state, action):
        actions_to_exclude = self.get_actions_to_exclude(state)
        return action.id() in actions_to_exclude and cfg.crawler_config['action']['should_exclude_duplicates']


    def add_neighbor_to_state(self, state, action, neighbor_state):
        state.add_neighbor(action, neighbor_state)
    
    
    def action_lead_to_invalid_domain(self, state):
        prev_state_domain = urlparse(state.url, scheme='', allow_fragments=True).netloc
        new_state_domain = urlparse(driver.current_url, scheme='', allow_fragments=True).netloc
        return prev_state_domain != new_state_domain

    
    def add_neighbor_if_not_same_state(self, state, action):
        body = driver.find_element(By.TAG_NAME, 'body')
        new_state = State(
            driver.current_url,
            body.get_attribute('outerHTML'),
            body.text,
            state,
            action
        )
        
        if state != new_state:
            self.add_neighbor_to_state(state, action, new_state)

    
    def execute_single_action(self, action, retries):
        try:
            logger.debug(f'Executing: {action}')
            
            action.execute()
            action.set_execution_result((True, None))
                
            time.sleep(cfg.crawler_config['wait']['after_action'])
            
            return True
        except Exception as e:
            logger.debug(f'Exception: {e}')
            
            if retries + 1 < cfg.crawler_config['action']['max_retries_after_fail']:
                logger.debug(f'{action} failed {retries + 1} times. Retrying Later.')
                return False
            else:
                logger.debug(f'{action} failed {retries + 1} times. Skipping.')
                return True
    
    
    def execute_actions(self, state):
        action_execution_queue = self.create_action_execution_queue(state.actions)
        
        while len(action_execution_queue) > 0:
            action, retries = action_execution_queue.pop(0)
            
            # might cause problems in an SPA application where URL won't change but content will
            if self.should_exclude_action(state, action):
                self.add_neighbor_to_state(
                    state,
                    action,
                    self.get_executed_actions_in_url(state.url)[action.id()]
                )
                logger.debug(f'Skipping: {action}')
                continue
            
            if action.outer_domain:
                logger.debug(f'Skipping: {action} (outer domain)')
                continue
            
            action_execution_success = self.execute_single_action(action, retries)
            
            if not action_execution_success:
                action_execution_queue.append((action, retries + 1))
                continue
            
            if self.action_lead_to_invalid_domain(state):
                logger.info('Action leads to invalid domain')
                action.outer_domain = True
                continue
            
            self.add_neighbor_if_not_same_state(state, action)
            self.add_state_actions_to_map(state)
            
            state.get_to_state()
