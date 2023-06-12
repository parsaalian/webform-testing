from selenium.webdriver.common.by import By


def get_xpath(driver, element):
    xpath_script = """
    function getPathTo(element) {
        // if (element.id !== '')
        //     return 'id(\"'+element.id+'\")';
        if (element === document.body)
            return element.tagName;
        var ix= 0;
        var siblings= element.parentNode.childNodes;
        for (var i= 0; i<siblings.length; i++) {
            var sibling= siblings[i];
            if (sibling===element)
                return getPathTo(element.parentNode) + '/' + element.tagName + '[' + (ix + 1) + ']';
            if (sibling.nodeType===1 && sibling.tagName===element.tagName)
                ix++;
        }
    }
    const path = getPathTo(arguments[0]);
    if (path.startsWith('id(')) {
        return path;
    }
    return '//' + path;
    """
    return driver.execute_script(xpath_script, element)


def get_visual_spans(element):
    # Get the location and size of the root element
    location = element.location
    size = element.size

    # Calculate the boundaries of the root element
    x_span = (location['x'], location['x'] + size['width'])
    y_span = (location['y'], location['y'] + size['height'])
    
    return x_span, y_span


def set_attribute(driver, element, key, value):
    driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", element, key, value)


def embed_properties(driver, root):
    '''
    This function embeds the x_span, y_span, and xpath
    properties into WebElement as attributes for processing
    in the next steps. We do this because we want to convert
    the WebElement into a BeautifulSoup document.
    '''
    x_span, y_span = get_visual_spans(root)
    xpath = get_xpath(driver, root)
    
    set_attribute(driver, root, 'xpath', xpath)
    set_attribute(driver, root, 'x_start', x_span[0])
    set_attribute(driver, root, 'x_end', x_span[1])
    set_attribute(driver, root, 'y_start', y_span[0])
    set_attribute(driver, root, 'y_end', y_span[1])
    
    for child in root.find_elements(By.XPATH, '*'):
        embed_properties(driver, child)
    
    return root