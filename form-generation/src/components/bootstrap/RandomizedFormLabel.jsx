// TODO: improve randomization rules
import React from 'react'
import Form from 'react-bootstrap/Form';
import randomWords from 'random-words';

function RandomizedFormLabel(props) {
    const text = randomWords({ min: 1, max: 3, join: ' ' });

    return (
        <Form.Label {...props}>
            {text}
        </Form.Label>
    )
}

export default RandomizedFormLabel;