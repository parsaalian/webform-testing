import { Radio } from 'antd';
import { BooleanInputParameterDistribution } from '../../models/distribution/inputs/booleanInput';
import { RadioMapper } from '../../models/libraries/antd/mappers/radioMapper';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignRadio() {
    return (
        <AntDesignInputItem
            Distribution={BooleanInputParameterDistribution}
            Mapper={RadioMapper}
            hasExternalLabel={false}
        >
            {({
                disabled,
                defaultValue,
                label,
            }) => (
                <Radio
                    disabled={disabled}
                    defaultChecked={defaultValue}
                >
                    {label}
                </Radio>
            )}
        </AntDesignInputItem>
    );
}