from __future__ import annotations

from selenium.webdriver.remote.webelement import WebElement


class ParseEntry:
    def __init__(
        self,
        label: str | None = None,
        tag: str | None = None,
        attributes: dict[str, any] | None = None,
        element: WebElement | None = None,
    ):
        self.label = label
        self.tag = tag
        self.attributes = attributes
        self.element = element
