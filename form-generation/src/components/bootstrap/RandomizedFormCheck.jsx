import React from 'react'
import Form from 'react-bootstrap/Form';
import random from 'random';
import randomWords from 'random-words';

function RandomizedFormCheck({ inline, ...props }) {
    const id = randomWords();
    const disabled = random.choice([false, true]);
    const feedbackTooltip = random.choice([false, true]);
    const isInvalid = random.choice([false, true]);
    const isValid = !isInvalid && random.choice([false, true]);
    const type = random.choice(['checkbox', 'radio', 'switch']);
    const label = random.choice(['', randomWords({ min: 1, max: 5, join: ' ' })]);
    const feedback = random.choice([null, randomWords({ min: 3, max: 10, join: ' '})])

    if (type === 'switch') {
        return (
            <Form.Check
                id={id}
                disabled={disabled}
                feedbackTooltip={feedbackTooltip}
                isInvalid={isInvalid}
                isValid={isValid}
                inline={inline}
                type={type}
                label={label}
                feedback={feedback}
                {...props}
            />
        )
    }

    return (
        <Form.Check
            id={id}
            disabled={disabled}
            feedbackTooltip={feedbackTooltip}
            isInvalid={isInvalid}
            isValid={isValid}
            inline={inline}
            type={type}
            {...props}
        >
            <Form.Check.Input
                isInvalid={isInvalid}
                isValid={isValid}
                type={type}
            />
            <Form.Check.Label>{label}</Form.Check.Label>
            <Form.Control.Feedback type={isValid ? 'valid' : 'invalid'}>{feedback}</Form.Control.Feedback>
        </Form.Check>
    )
}

export default RandomizedFormCheck;