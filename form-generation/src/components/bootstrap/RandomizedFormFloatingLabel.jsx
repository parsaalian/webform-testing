import React from 'react'
import Form from 'react-bootstrap/Form';
import randomWords from 'random-words';
import RandomizedFormLabel from './RandomizedFormLabel';

function RandomizedFormFloatingLabel({ children }) {
    const controlId = randomWords({ exactly: 3, join: '-' });

    const childrenWithProps = React.Children.map(children, child => {
        if (React.isValidElement(child)) {
            return React.cloneElement(child, { id: controlId });
        }
        return child;
    });

    return (
        <Form.Floating>
            {childrenWithProps}
            <RandomizedFormLabel for={controlId} />
        </Form.Floating>
    )
}

export default RandomizedFormFloatingLabel;