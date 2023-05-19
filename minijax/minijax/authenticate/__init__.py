from minijax.config import Config
from minijax.authenticate.addressbook_auth import authenticate_addressbook

cfg = Config()


def authenticate():
    if cfg.app_config['application_name'] == 'addressbook':
        authenticate_addressbook()


__all__ = [
    'authenticate',
]