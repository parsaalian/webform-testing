// TODO: improve randomization rules
import React from 'react'
import Form from 'react-bootstrap/Form';
import random from 'random';
import randomWords from 'random-words';

function RandomizedFormSelect(props) {
    const optionsCount = 1 + random.poisson(3)();
    let options = [];
    for (let i = 0; i < optionsCount; i++) {
        options = [...options, randomWords({ min: 1, max: 3, join: ' ' })];
    }

    const disabled = random.choice([false, true]);
    const isInvalid = random.choice([false, true]);
    const isValid = !isInvalid && random.choice([false, true]);
    const size = random.choice([null, 'sm', 'lg']);

    const htmlSize = 1 + random.poisson(1)();

    return (
        <Form.Select
            htmlSize={htmlSize}
            disabled={disabled}
            isInvalid={isInvalid}
            isValid={isValid}
            size={size}
            {...props}
        >
            {options.map((option, i) => (
                <option key={i}>{option}</option>
            ))}
        </Form.Select>
    )
}

export default RandomizedFormSelect;