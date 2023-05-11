import os
import time
import json

from minijax.config import Config


def create_report_directory(report_name):
    cfg = Config()
    base_dir = cfg.crawler_config['report_directory']
    if not os.path.exists(base_dir):    
        os.makedirs(base_dir)
    report_base_dir = os.path.join(base_dir, report_name)
    if not os.path.exists(report_base_dir):
        os.makedirs(report_base_dir)


def generate_report(app_title, state_graph):
    cfg = Config()
    time_str = time.strftime("%Y%m%d-%H%M%S")
    
    report_name = f'{time_str}-{app_title}'
    create_report_directory(report_name)
    
    graph = state_graph.to_json()
    graph_path = os.path.join(cfg.crawler_config['report_directory'], report_name, 'graph.json')
    json.dump(graph, open(graph_path, 'w'), indent=4)
    
    report = {
        'url_coverage': state_graph.count_urls(),
        'state_coverage': state_graph.count_states(),
    }
    report_path = os.path.join(cfg.crawler_config['report_directory'], report_name, 'report.json')
    json.dump(report, open(report_path, 'w'), indent=4)
    
    config_json = cfg.to_json()
    config_path = os.path.join(cfg.crawler_config['report_directory'], report_name, 'config.json')
    json.dump(config_json, open(config_path, 'w'), indent=4)