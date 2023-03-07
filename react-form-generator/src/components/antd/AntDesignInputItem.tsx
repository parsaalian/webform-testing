import { Form } from 'antd';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';

export default function AntDesignInputItem({
    Distribution,
    Mapper,
    hasExternalLabel,
    children,
}) {
    const props = LibraryComponentGenerator.generateComponent(
        new Distribution(),
        Mapper,
    );

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