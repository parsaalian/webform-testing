import time
import hashlib

from selenium.webdriver.common.by import By

from minijax.config import Config
from minijax.crawler import get_driver_container
from minijax.crawler.utils import get_element_xpath
from minijax.crawler.action import (
    GoToRootAction,
    FormAction,
    ClickAction,
)
from minijax.form.finder import find_forms_by_query


cfg = Config()
driver = get_driver_container().get_driver()


class State:
    def __init__(self, url, html, text, prev_state, prev_action):
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
    
    
    def find_form_actions(self):
        # TODO: change based on different finding modes
        forms = find_forms_by_query(driver)
        # if cfg.model_config['workflow'].form_finder_mode == FormFinderMode.BASIC:
        #     forms = find_forms_by_query(driver)
        # else:
        #     forms = find_forms_by_query(driver)
        
        # TODO: write a common function for all different action types
        forms = list(filter(lambda x: x.is_displayed(), forms))
        forms_xpath = list(map(
            lambda x: get_element_xpath(driver, x),
            forms
        ))
        forms_actions = list(map(
            lambda x: FormAction(
                xpath=x,
                parent_state=self,
            ),
            forms_xpath
        ))
        return forms_actions

    
    def find_click_actions(self):
        tags = driver.find_elements(By.TAG_NAME, 'a')
        tags = list(filter(lambda x: x.is_displayed(), tags))
        tags_xpath = list(map(
            lambda x: get_element_xpath(driver, x),
            tags
        ))
        tags_actions = list(map(
            lambda x: ClickAction(
                xpath=x,
                parent_state=self
            ),
            tags_xpath
        ))
        return tags_actions

    
    def find_hover_actions(self):
        return []
    
    
    def _eval_actions(self):
        actions = []
        
        click_actions = self.find_click_actions()
        hover_actions = self.find_hover_actions()
        form_actions = self.find_form_actions()
        
        if cfg.crawler_config['action']['enabled']['click']:
            actions = [*actions, *click_actions]
        if cfg.crawler_config['action']['enabled']['hover']:
            actions = [*actions, *hover_actions]
        if cfg.crawler_config['action']['enabled']['form']:
            actions = [*actions, *form_actions]
        
        self.actions = actions
    
    
    def add_neighbor(self, action, neighbor_state):
        self.neighbors[action.id()] = neighbor_state
    
    
    def get_to_state(self):
        for action in self.root_path:
            action.execute()
            time.sleep(cfg.crawler_config['wait']['after_action'])
    
    
    def get_neighbors(self):
        return self.neighbors
    
    
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
