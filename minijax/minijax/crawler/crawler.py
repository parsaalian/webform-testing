from selenium.webdriver.common.by import By

from minijax.logger import logger
from minijax.config import Config
from minijax.authenticate import authenticate
from minijax.crawler.report import generate_report
from minijax.crawler import get_driver_container
from minijax.crawler.state import State, StateGraph, StateActionExecutioner


cfg = Config()
driver = get_driver_container().get_driver()


class Crawler:
    def __init__(self):
        self.state_graph = StateGraph()
        self.state_action_executioner = StateActionExecutioner()
        self.title = None
    
    
    def crawl(self):
        counter = 0
        
        driver.get(cfg.app_url)
        self.title = driver.title
        body = driver.find_element(By.TAG_NAME, 'body')
        initial_state = State(
            driver.current_url,
            body.get_attribute('outerHTML'),
            body.text,
            None,
            None,
        )
        crawl_queue = [initial_state]
        self.state_graph.add_state(initial_state)
        
        while len(crawl_queue) > 0 and counter < cfg.crawler_config['max_crawling_iterations']:
            counter += 1
            logger.info(f"\n===================\nIteration: {counter}")

            state = crawl_queue[0]
            
            state.get_to_state()
            
            logger.info(f"Crawling state: {state}")
            
            self.state_action_executioner.execute_actions(state)
            
            for _, neighbor_state in state.get_neighbors().items():
                if not self.state_graph.is_in_graph(neighbor_state):
                    self.state_graph.add_state(neighbor_state)
                    crawl_queue.append(neighbor_state)
            
            crawl_queue = crawl_queue[1:]
    
    
    def start(self):
        if cfg.app_config['has_auth']:
            authenticate()
        self.crawl()
        generate_report(self.title, self.state_graph)