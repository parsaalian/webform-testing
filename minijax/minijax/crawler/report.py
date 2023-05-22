import os
import time
import json

from minijax.config import Config
from minijax.utils import Singleton


cfg = Config()


class Reporter(metaclass=Singleton):
    def __init__(self, app_title):
        self.directory = None
        
        self._create_report_directory(app_title)
    
    
    def get_directory(self):
        return self.directory
    
    
    def _create_report_directory(self, app_title):
        time_str = time.strftime("%Y%m%d-%H%M%S")
        
        report_name = f'{time_str}-{app_title}'
        
        base_dir = cfg.crawler_config['report_directory']
        if not os.path.exists(base_dir):    
            os.makedirs(base_dir)
        report_base_dir = os.path.join(base_dir, report_name)
        if not os.path.exists(report_base_dir):
            os.makedirs(report_base_dir)
        screenshot_base_dir = os.path.join(report_base_dir, 'screenshots')
        if not os.path.exists(screenshot_base_dir):
            os.makedirs(screenshot_base_dir)
        self.directory = report_base_dir


    def generate_report(self, state_graph):
        graph = state_graph.to_json()
        graph_path = os.path.join(self.directory, 'graph.json')
        json.dump(graph, open(graph_path, 'w'), indent=4)
        
        report = {
            'url_coverage': state_graph.count_urls(),
            'state_coverage': state_graph.count_states(),
        }
        report_path = os.path.join(self.directory, 'report.json')
        json.dump(report, open(report_path, 'w'), indent=4)
        
        config_json = cfg.to_json()
        config_path = os.path.join(self.directory, 'config.json')
        json.dump(config_json, open(config_path, 'w'), indent=4)