from minijax.crawler import get_driver_container
from minijax.config import Config
from minijax.crawler.action.base import ActionBase


class GoToRootAction(ActionBase):
    def __init__(self):
        super().__init__(None)
    
    
    def execute(self):
        cfg = Config()
        driver = get_driver_container().get_driver()
        driver.get(cfg.app_url)
    
    
    def id(self):
        return 'go_to_root'
