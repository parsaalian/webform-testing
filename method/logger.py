"""Logging module"""
"""based on: https://github.com/Significant-Gravitas/Auto-GPT/blob/master/autogpt/logs.py"""
import logging
import os
import re
from logging import LogRecord
from typing import Any

from colorama import Fore, Style

from method.utils import Singleton


class Logger(metaclass=Singleton):
    """
    Logger that handle titles in different colors.
    Outputs logs in console, activity.log, and errors.log
    For console handler: simulates typing
    """

    def __init__(self):
        # create log directory if it doesn't exist
        this_files_dir_path = os.path.dirname(__file__)
        log_dir = os.path.join(this_files_dir_path, "../logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = "activity.log"
        error_file = "error.log"

        console_formatter = AutoGptFormatter("%(title_color)s %(message)s")

        # Create a handler for console without typing simulation
        self.console_handler = ConsoleHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(console_formatter)

        # Info handler in activity.log
        self.file_handler = logging.FileHandler(
            os.path.join(log_dir, log_file), "a", "utf-8"
        )
        self.file_handler.setLevel(logging.DEBUG)
        info_formatter = AutoGptFormatter(
            "%(asctime)s %(levelname)s %(title)s %(message_no_color)s"
        )
        self.file_handler.setFormatter(info_formatter)

        # Error handler error.log
        error_handler = logging.FileHandler(
            os.path.join(log_dir, error_file), "a", "utf-8"
        )
        error_handler.setLevel(logging.ERROR)
        error_formatter = AutoGptFormatter(
            "%(asctime)s %(levelname)s %(module)s:%(funcName)s:%(lineno)d %(title)s"
            " %(message_no_color)s"
        )
        error_handler.setFormatter(error_formatter)

        self.logger = logging.getLogger("LOGGER")
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(error_handler)
        self.logger.setLevel(logging.DEBUG)


    def debug(self, message, title="", title_color=""):
        self._log(title, title_color, message, logging.DEBUG)


    def info(self, message, title="", title_color=""):
        self._log(title, title_color, message, logging.INFO)


    def warn(self, message, title="", title_color=""):
        self._log(title, title_color, message, logging.WARN)


    def error(self, title, message=""):
        self._log(title, Fore.RED, message, logging.ERROR)


    def _log(self, title: str = "", title_color: str = "", message: str = "", level=logging.INFO):
        if message:
            if isinstance(message, list):
                message = " ".join(message)
        self.logger.log(
            level, message, extra={"title": str(title), "color": str(title_color)}
        )


    def set_level(self, level):
        self.logger.setLevel(level)
        self.typing_logger.setLevel(level)
    

    def get_log_directory(self):
        this_files_dir_path = os.path.dirname(__file__)
        log_dir = os.path.join(this_files_dir_path, "../logs")
        return os.path.abspath(log_dir)


class ConsoleHandler(logging.StreamHandler):
    def emit(self, record) -> None:
        msg = self.format(record)
        try:
            print(msg)
        except Exception:
            self.handleError(record)


class AutoGptFormatter(logging.Formatter):
    """
    Allows to handle custom placeholders 'title_color' and 'message_no_color'.
    To use this formatter, make sure to pass 'color', 'title' as log extras.
    """

    def format(self, record: LogRecord) -> str:
        if hasattr(record, "color"):
            record.title_color = (
                getattr(record, "color")
                + getattr(record, "title", "")
                + " "
                + Style.RESET_ALL
            )
        else:
            record.title_color = getattr(record, "title", "")

        # Add this line to set 'title' to an empty string if it doesn't exist
        record.title = getattr(record, "title", "")

        if hasattr(record, "msg"):
            record.message_no_color = remove_color_codes(getattr(record, "msg"))
        else:
            record.message_no_color = ""
        return super().format(record)


def remove_color_codes(s: str) -> str:
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", s)


logger = Logger()
