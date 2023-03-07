import { Checkbox } from 'antd';
import { BooleanInputParameterDistribution } from '../../models/distribution/inputs/booleanInput';
import { CheckboxMapper } from '../../models/libraries/antd/mappers/checkboxMapper';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignCheckbox() {
    return (
        <AntDesignInputItem
            Distribution={BooleanInputParameterDistribution}
            Mapper={CheckboxMapper}
            hasExternalLabel={false}
        >
            {({
                disabled,
                defaultValue,
                indeterminate,
                label,
            }) => (
                <Checkbox
                    disabled={disabled}
                    defaultChecked={defaultValue}
                    indeterminate={indeterminate}
                >
                    {label}
                </Checkbox>
            )}
        </AntDesignInputItem>
    );
}