import os

from minijax.utils import Singleton


class Config(metaclass=Singleton):
    def __init__(self):
        self.app_url = os.getenv('APP_URL', 'https://www.google.com')
    
    
    def set_app_url(self, app_url):
        self.app_url = app_url
    
    
    def set_crawler_config(self, crawler_config):
        self.crawler_config = crawler_config
    
    
    def set_model_config(self, model_config):
        self.model_config = model_config
    
    
    def set_llm_config(self, llm_config):
        openai_api_key = os.getenv('OPENAI_API_KEY', None)
        if openai_api_key is not None:
            llm_config['openai_api_key'] = openai_api_key
        self.llm_config = llm_config
    
    
    def to_json(self):
        return {
            'app_url': self.app_url,
            'crawler_config': self.crawler_config,
            'model_config': self.model_config,
            'llm_config': self.llm_config,
        }
