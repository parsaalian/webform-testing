import os
import yaml

from minijax.config import Config
from minijax.crawler import get_driver_container, Crawler


def run_crawler(
    url,
    debug,
    crawler_config_path,
    model_config_path,
):
    cfg = Config()
    crawler_config = yaml.load(open(crawler_config_path, 'r'), Loader=yaml.FullLoader)
    model_config = yaml.load(open(model_config_path, 'r'), Loader=yaml.FullLoader)
    
    if url is not None:
        cfg.set_app_url(url)
    cfg.set_debug(debug)
    cfg.set_crawler_config(crawler_config)
    cfg.set_model_config(model_config)
    
    try:
        crawler = Crawler()
        crawler.start()
    finally:
        driver = get_driver_container().get_driver()
        driver.quit()
