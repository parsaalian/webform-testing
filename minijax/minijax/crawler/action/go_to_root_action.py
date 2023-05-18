from minijax.crawler import get_driver_container
from minijax.config import Config
from minijax.crawler.action.base import ActionBase


cfg = Config()
driver = get_driver_container().get_driver()


class GoToRootAction(ActionBase):
    def __init__(self):
        super().__init__(None, None)
    
    
    def execute(self):
        driver.get(cfg.app_url)
    
    
    def retry(self):
        self.execute()
    
    
    def id(self):
        return 'go_to_root'
