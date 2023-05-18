import os

from minijax.utils import Singleton


class Config(metaclass=Singleton):
    def __init__(self):
        self.app_url = os.getenv('APP_URL', 'https://www.google.com')
        self.debug = os.getenv('DEBUG', False)
        
        self.openai_api_key = os.getenv('OPENAI_API_KEY', None)
    
    
    def set_app_url(self, app_url):
        self.app_url = app_url
    
    
    def set_debug(self, debug):
        self.debug = debug
    
    
    def set_crawler_config(self, crawler_config):
        self.crawler_config = crawler_config
    
    
    def set_model_config(self, model_config):
        self.model_config = model_config
    
    
    def set_auth_config(self, auth_config):
        self.auth_config = auth_config
    
    
    def to_json(self):
        return {
            'app_url': self.app_url,
            'debug': self.debug,
            'crawler_config': self.crawler_config,
            'model_config': self.model_config,
            'auth_config': self.auth_config,
        }
