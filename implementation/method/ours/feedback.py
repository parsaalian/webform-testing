from bs4 import BeautifulSoup
from deepdiff import DeepDiff


feedback_keywords = [
    'invalid',
    'required',
    'error',
    'not possible',
    'missing',
    'failed',
    'incorrect',
    'retry',
    'verify',
    'exceeds',
    'denied',
    'please enter',
    'format',
    'does not match',
    'try again',
    'unavailable',
    'warning',
    'out of range',
    'unable to',
    'not recognized',
    'not allowed',
    'incomplete',
    'cannot process',
    'duplicate',
    'too short',
    'too long',
    'doesn\'t exist',
    'does not exist',
    'already exist',
    'authentication failed',
    'expired',
    'update failed',
    'connection',
    'server error',
    'system error',
    'not valid',
    'timed out',
    'access denied',
    'please confirm',
    'not acceptable',
    'submission failed',
    'unexpected',
    'conflict',
    'not applicable',
    'not active',
    'not found',
    'not secure',
    'forbidden',
    'disconnect',
    'prohibited',
]


def has_feedback_keyword(sentence):
    for keyword in feedback_keywords:
        if keyword in sentence:
            return True
    return False


def get_global_feedback(html1, html2):
    # Parse the HTML.
    soup1 = BeautifulSoup(html1, 'html.parser')
    soup2 = BeautifulSoup(html2, 'html.parser')

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
    
    changes = list(filter(lambda x: x.strip() != '', map(lambda x: x.text.strip(), changes)))
    
    changes = list(filter(has_feedback_keyword, changes))
    
    return changes


def get_local_feedback(input_group):
    local_feedback = list(
        map(
            lambda x: x.target.element.text,
            filter(
                lambda x: x.type.value == 'P_FEEDBACK',
                input_group.node.edges.values()
            )
        )
    )
    
    return local_feedback