def get_element_xpath(driver, element):
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
    
    xpath = driver.execute_script(xpath_script, element)
    return xpath