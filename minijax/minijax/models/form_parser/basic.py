from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from minijax.models.form_parser.parse_entry import ParseEntry


def basic_parse_form_inputs(form: WebElement) -> list(ParseEntry):
    inputs = inputs = form.find_elements(
        By.XPATH,
        "//*[self::input or self::textarea or self::select][not(@type = 'submit') and not(@type = 'hidden') and not(@hidden = 'true')]"
    )
    
    # turn into intended format
    inputs = list(map(
        lambda x: ParseEntry(
            label=None,
            tag=x.tag_name,
            attributes={
                attr["name"]: attr["value"] for attr in x.get_property('attributes')
            },
            element=x
        ),
        inputs
    ))
    
    return inputs
