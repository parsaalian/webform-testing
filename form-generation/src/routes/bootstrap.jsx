import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react'
import Form from 'react-bootstrap/Form';
import { BootstrapCheckbox } from '../models/library/bootstrap/bootstrapCheckbox.ts';

function Bootstrap() {
    const checkbox = new BootstrapCheckbox();
    return (
        <>
            <Form.Check
                {...checkbox}
            />
        </>
    );
}

export default Bootstrap;