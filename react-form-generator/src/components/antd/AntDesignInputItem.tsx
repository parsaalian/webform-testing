import { Form } from 'antd';

export default function AntDesignInputItem({
    hasExternalLabel,
    children,
    ...props
}) {
    const {
        label,
        required,
        validationState,
        validationMessage,
    } = props;

    return (
        <Form.Item
            hasFeedback={validationState !== ''}
            validateStatus={validationState}
            help={validationState !== '' ? validationMessage : ''}
            required={required}
            label={hasExternalLabel ? null : label}
        >
            {children(props)}
        </Form.Item>
    );
}