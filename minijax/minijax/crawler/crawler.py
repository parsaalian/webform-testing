from selenium.webdriver.common.by import By

from minijax.logger import logger
from minijax.config import Config
from minijax.crawler.report import generate_report
from minijax.crawler import get_driver_container
from minijax.crawler.state import State, StateGraph


class Crawler:
    def __init__(self):
        self.cfg = Config()
        self.driver = get_driver_container().get_driver()
        self.state_graph = StateGraph()
        self.title = None
    
    
    def crawl(self):
        counter = 0
        
        self.driver.get(self.cfg.app_url)
        self.title = self.driver.title
        body = self.driver.find_element(By.TAG_NAME, 'body')
        initial_state = State(
            self.driver.current_url,
            body.get_attribute('outerHTML'),
            body.text,
            None,
            None,
        )
        crawl_queue = [initial_state]
        self.state_graph.add_state(initial_state)
        
        while len(crawl_queue) > 0 and counter < self.cfg.crawler_config['max_crawling_iterations']:
            counter += 1
            logger.info(f"\n===================\nIteration: {counter}")

            next_state = crawl_queue[0]
            
            next_state.get_to_state()
            
            logger.info(f"Crawling state: {next_state}")
            
            next_state.execute_actions(
                actions_to_exclude=self.state_graph.get_executed_actions_in_url(next_state.url)
            )
            
            for action_id, neighbor_state in next_state.get_neighbors().items():
                if not self.state_graph.has_executed_action_in_url(next_state.url, action_id):
                    self.state_graph.add_executed_action_to_url(next_state.url, action_id, neighbor_state)
                
                if not self.state_graph.is_in_graph(neighbor_state):
                    self.state_graph.add_state(neighbor_state)
                    crawl_queue.append(neighbor_state)
            
            crawl_queue = crawl_queue[1:]
    
    
    def start(self):
        self.crawl()
        generate_report(self.title, self.state_graph)