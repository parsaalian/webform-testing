// TODO: improve randomization rules
import React from 'react'
import Form from 'react-bootstrap/Form';
import random from 'random';
import randomWords from 'random-words';

const htmlInputControls = [
    'input',
    'textarea',
];

const htmlInputTypes = [
    'color',
    'date',
    'datetime-local',
    'email',
    'file',
    'month',
    'number',
    'password',
    'search',
    'tel',
    'text',
    'time',
    'url',
    'week',
];

function getFormAs() {
    return random.choice(htmlInputControls);
}

function getDefaultValue(type) {
    switch (type) {
        case 'text':
            return random.choice([null, randomWords()]);
        case 'textarea':
            return random.choice([null, randomWords()]);
        case 'password':
            return random.choice([null, randomWords()]);
        case 'number':
            return random.uniformInt(-100, 100);
        default:
            return null;
    }
}

function getPlainText(type) {
    switch (type) {
        case 'text':
            return random.choice([false, true]);
        case 'textarea':
            return random.choice([false, true]);
        case 'password':
            return random.choice([false, true]);
        case 'number':
            return random.choice([false, true]);
        case 'email':
            return random.choice([false, true]);
        default:
            return false;
    }
}

function RandomizedFormControl(props) {
    const formAs = getFormAs()
    const disabled = random.choice([false, true]);
    const isInvalid = random.choice([false, true]);
    const isValid = !isInvalid && random.choice([false, true]);
    const plainTextAndReadOnly = getPlainText();
    const size = random.choice([null, 'sm', 'lg']);

    let type;
    if (formAs === 'input') {
        type = random.choice(htmlInputTypes);
    }
    else {
        type = 'text';
    }

    const defaultValue = getDefaultValue(type);
    const placeholder = getDefaultValue(type);

    let rows = null;
    if (formAs === 'textarea') {
        rows = 1 + random.poisson(2)();
    }

    return (
        <Form.Control
            as={formAs}
            defaultValue={defaultValue}
            disabled={disabled}
            isInvalid={isInvalid}
            isValid={isValid}
            placeholder={placeholder}
            plaintext={plainTextAndReadOnly}
            readOnly={plainTextAndReadOnly}
            size={size}
            type={type}
            rows={rows}
            {...props}
        />
    )
}

export default RandomizedFormControl;