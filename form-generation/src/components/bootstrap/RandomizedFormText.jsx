// TODO: improve randomization rules
import React from 'react'
import Form from 'react-bootstrap/Form';
import random from 'random';
import randomWords from 'random-words';

function RandomizedFormText(props) {
    const muted = random.choice([false, true]);
    const text = randomWords({ min: 3, max: 25, join: ' ' });

    return (
        <Form.Text
            muted={muted}
            {...props}
        >
            {text}
        </Form.Text>
    )
}

export default RandomizedFormText;