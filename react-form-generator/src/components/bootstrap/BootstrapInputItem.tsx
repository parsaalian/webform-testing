import { Form, FloatingLabel } from 'react-bootstrap';

export default function BootstrapInputItem({
    hasExternalLabel,
    hasExternalFeedback,
    children,
    ...props
}) {
    const {
        label,
        floating,
        validationState,
        validationMessage,
    } = props;

    if (floating) {
        return (
            <FloatingLabel
                label={label}
                className={validationState !== '' ? 'was-validated' : ''}
            >
                {children(props)}
                {validationMessage !== '' && <Form.Control.Feedback>{validationMessage}</Form.Control.Feedback>}
            </FloatingLabel>
        )
    }

    return (
        <Form.Group className={validationState !== '' ? 'was-validated' : ''}>
            {hasExternalLabel && label !== '' && <Form.Label>{label}</Form.Label>}
            {children(props)}
            {hasExternalFeedback && validationState !== '' && validationMessage !== '' &&
                <Form.Control.Feedback type={validationState}>
                    {validationMessage}
                </Form.Control.Feedback>
            }
        </Form.Group>
    );
}