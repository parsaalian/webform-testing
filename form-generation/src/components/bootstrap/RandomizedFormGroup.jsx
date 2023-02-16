// TODO: add validation
import React from 'react'
import Form from 'react-bootstrap/Form';
import random from 'random';

import RandomizedFormLabel from './RandomizedFormLabel';
import RandomizedFormText from './RandomizedFormText';
import RandomizedFormCheck from './RandomizedFormCheck';
import RandomizedFormCheckGroup from './RandomizedFormCheckGroup';
import RandomizedFormControl from './RandomizedFormControl';
import RandomizedFormFloatingLabel from './RandomizedFormFloatingLabel';
import RandomizedFormInputGroup from './RandomizedFormInputGroup';
import RandomizedFormRange from './RandomizedFormRange';
import RandomizedFormSelect from './RandomizedFormSelect';

function RandomizedFormGroup(props) {
    const floating = random.choice([false, true]);
    const hasText = random.choice([false, true]);

    let RandomizedElement;
    if (floating) {
        RandomizedElement = random.choice([
            RandomizedFormControl,
            RandomizedFormSelect,
        ]);

        return (
            <Form.Group {...props}>
                <RandomizedFormFloatingLabel>
                    <RandomizedElement />
                </RandomizedFormFloatingLabel>
                {hasText && <RandomizedFormText />}
            </Form.Group>
        );
    }

    RandomizedElement = random.choice([
        RandomizedFormCheck,
        RandomizedFormCheckGroup,
        RandomizedFormControl,
        RandomizedFormRange,
        RandomizedFormSelect,
        RandomizedFormInputGroup,
    ]);

    return (
        <Form.Group {...props}>
            {(RandomizedElement.displayName !== 'RandomizedFormCheckGroup'
                || RandomizedElement.displayName !== 'RandomizedFormCheck'
            ) && <RandomizedFormLabel />}
            <RandomizedElement />
            {hasText && <RandomizedFormText />}
        </Form.Group>
    )
}

export default RandomizedFormGroup;