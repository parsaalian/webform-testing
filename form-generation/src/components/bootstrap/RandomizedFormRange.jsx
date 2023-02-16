import React from 'react'
import Form from 'react-bootstrap/Form';
import random from 'random';
import RandomizedFormLabel from './RandomizedFormLabel';

function RandomizedFormRange(props) {
    const value = random.uniformInt(-100, 100)();

    return (
        <>
            <RandomizedFormLabel />
            <Form.Range min={-100} max={100} defaultValue={value} />
        </>
    );
}

export default RandomizedFormRange;