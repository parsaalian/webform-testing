import { Form, Select } from 'antd';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { SelectParameterDistribution } from '../../models/interfaces/distribution/inputs/select';
import { SelectMapper } from '../../models/libraries/antd/mappers/selectMapper';

export default function AntDesignSelect() {
    const {
        label,
        disabled,
        required,
        validationState,
        validationMessage,
        options,
        defaultValue,
        mode,
    } = LibraryComponentGenerator.generateComponent(
        new SelectParameterDistribution(),
        SelectMapper
    );

    return (
        <Form.Item
            hasFeedback={validationState !== ''}
            validateStatus={validationState}
            help={validationState !== '' ? validationMessage : ''}
            required={required}
            label={label}
        >
            <Select
                disabled={disabled}
                defaultValue={defaultValue}
                mode={mode}
            >
                {options.map((option) => (
                    <Select.Option key={option.value} value={option.value}>
                        {option.label}
                    </Select.Option>
                ))}
            </Select>
        </Form.Item>
    );
}