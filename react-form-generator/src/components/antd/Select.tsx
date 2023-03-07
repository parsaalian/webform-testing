import { Select } from 'antd';
import { SelectParameterDistribution } from '../../models/distribution/inputs/select';
import { SelectMapper } from '../../models/libraries/antd/mappers/selectMapper';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignSelect() {
    return (
        <AntDesignInputItem
            Distribution={SelectParameterDistribution}
            Mapper={SelectMapper}
            hasExternalLabel={true}
        >
            {({
                disabled,
                defaultValue,
                mode,
                options,
            }) => (
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
            )}
        </AntDesignInputItem>
    );
}