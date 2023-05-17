from minijax.config import Config


cfg = Config()


def raise_in_debug_mode(exception):
    if cfg.debug:
        raise Exception(exception)
    pass