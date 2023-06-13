from bs4 import NavigableString, Comment


def is_displayed(element):
    if isinstance(element, NavigableString):
        return True
    
    x_start = float(element.attrs['x_start'])
    x_end = float(element.attrs['x_end'])
    y_start = float(element.attrs['y_start'])
    y_end = float(element.attrs['y_end'])
    
    return x_start != x_end and y_start != y_end


def should_skip_processing(element):
    should_skip = \
        isinstance(element, Comment) or \
        (isinstance(element, NavigableString) and element.strip() == '') or \
        not is_displayed(element)
    return should_skip


def is_force_not_keep(element):
    # TODO: list of elements not to keep, like children of svg
    if element.name == 'svg' or element.name == 'path':
        return True

    return False


def is_force_keep(element):
    force_keep_tags = ['label', 'input', 'textarea', 'select', 'option', 'button']
    return element.name in force_keep_tags
    


def has_action_listener(element):
    # TODO: check if element has JavaScript action listeners
    # such as the case of <div> instead of <button> for submit
    return False


def is_processable(element):
    if not isinstance(element, NavigableString) and is_force_not_keep(element):
        return False
    
    if isinstance(element, NavigableString):
        if element.parent is not None and len(element.parent.contents) > 1:
            return True
    
    elif len(element.contents) == 0:
        return True
    
    elif len(element.contents) == 1 and isinstance(element.contents[0], NavigableString):
        return True
    
    elif is_force_keep(element):
        return True
    
    elif has_action_listener(element):
        return True
    
    return False


def wrap_free_text(doc):
    should_wrap = []

    for element in doc.recursiveChildGenerator():
        if isinstance(element, NavigableString) and \
            element.parent is not None and \
            len(element.parent.contents) > 1:
            
            should_wrap.append(element)

    for idx, element in enumerate(should_wrap):
        span = doc.new_tag('span-wrap')
        span.string = element.string
        span.attrs = {
            "x_start": "0",
            "x_end": "0",
            "y_start": "0",
            "y_end": "0",
            "xpath": f"{element.parent.attrs['xpath']}/SPAN-WRAP[{idx + 1}]"
        }
        element.insert_before(span)
        element.extract()
    
    return doc


def get_processable_nodes(soup):
    nodes = []
    
    soup = wrap_free_text(soup)
    
    for element in soup.recursiveChildGenerator():
        if should_skip_processing(element):
            continue
        
        if is_processable(element):
            nodes.append(element)
    
    return nodes