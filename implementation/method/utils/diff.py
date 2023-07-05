from bs4 import BeautifulSoup as bs
from deepdiff import DeepDiff


def get_html_diff(html1, html2):
    # Parse the HTML.
    soup1 = bs(html1, 'html.parser')
    soup2 = bs(html2, 'html.parser')

    # Find the differences.
    diff = DeepDiff(soup1, soup2)

    changes = []

    if 'type_changes' in diff:
        for type_change in diff['type_changes'].values():
            changes.append(type_change['new_value'])

    if 'values_changed' in diff:
        for value_change in diff['values_changed'].values():
            changes.append(value_change['new_value'])

    if 'iterable_item_added' in diff:
        for iterable_item in diff['iterable_item_added'].values():
            changes.append(iterable_item)
    
    
    return changes