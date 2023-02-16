// TODO: use randomized button and text
import React from 'react'
import Button from 'react-bootstrap/Button';
import InputGroup from 'react-bootstrap/InputGroup';
import random from 'random';
import randomWords from 'random-words';
import RandomizedFormControl from './RandomizedFormControl';

function RandomizedFormInputGroup() {
    const begin = random.poisson(1)();
    const inputs = 1 + random.poisson(1)();
    const end = random.poisson(1)();
    
    let parts = [];
    for (let i = 0; i < begin; i++) {
        parts = [...parts, random.choice(['text', 'button'])];
    }
    for (let i = 0; i < inputs; i++) {
        parts = [...parts, 'input'];
    }
    for (let i = 0; i < end; i++) {
        parts = [...parts, random.choice(['text', 'button'])];
    }

    return (
        <InputGroup>
            {parts.map((part, i) => {
                if (part === 'text') {
                    return (
                        <InputGroup.Text>{randomWords()}</InputGroup.Text>
                    );
                }
                if (part === 'button') {
                    return (
                        <Button variant="outline-secondary">{randomWords()}</Button>
                    );
                }
                return <RandomizedFormControl />
            })}
        </InputGroup>
    );
}

export default RandomizedFormInputGroup;