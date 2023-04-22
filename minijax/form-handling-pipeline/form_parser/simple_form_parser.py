from selenium.webdriver.common.by import By


def parse_form_inputs_without_labels(form):
    inputs = form.find_elements(By.TAG_NAME, 'input')
    
    inputs = list(filter(
        lambda x: x.get_attribute('type') != 'hidden',
        inputs
    ))
    
    inputs = list(map(
        lambda x: {
            "label": None,
            "tag": x.tag_name,
            "attributes": {
                attr["name"]: attr["value"] for attr in x.get_property('attributes')
            },
            "element": x
        },
        inputs
    ))
    return inputs