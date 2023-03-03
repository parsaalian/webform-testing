import { Form, Cascader } from 'antd';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { SelectParameterDistribution } from '../../models/interfaces/distribution/inputs/select';
import { CascaderMapper } from '../../models/libraries/antd/mappers/cacaderMapper';

export default function AntDesignCascader() {
    const {
        label,
        disabled,
        required,
        validationState,
        validationMessage,
        options,
        defaultValue,
        multiple,
    } = LibraryComponentGenerator.generateComponent(
        new SelectParameterDistribution(),
        CascaderMapper
    );

    return (
        <Form.Item
            hasFeedback={validationState !== ''}
            validateStatus={validationState}
            help={validationState !== '' ? validationMessage : ''}
            required={required}
            label={label}
        >
            <Cascader
                disabled={disabled}
                defaultValue={defaultValue}
                multiple={multiple}
                options={options}
            />
        </Form.Item>
    );
}