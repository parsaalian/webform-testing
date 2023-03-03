import { Form, Checkbox } from 'antd';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { BooleanInputParameterDistribution } from '../../models/interfaces/distribution/inputs/booleanInput';
import { CheckboxMapper } from '../../models/libraries/antd/mappers/checkboxMapper';

export default function AntDesignCheckbox() {
    const {
        label,
        disabled,
        required,
        defaultChecked,
        indeterminate,
        validationState,
        validationMessage,
    } = LibraryComponentGenerator.generateComponent(
        new BooleanInputParameterDistribution(),
        CheckboxMapper
    );

    return (
        <Form.Item
            hasFeedback={validationState !== ''}
            validateStatus={validationState}
            help={validationState !== '' ? validationMessage : ''}
            required={required}
        >
            <Checkbox
                disabled={disabled}
                defaultChecked={defaultChecked}
                indeterminate={indeterminate}
            >
                {label}
            </Checkbox>
        </Form.Item>
    );
}