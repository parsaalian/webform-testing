import { Cascader } from 'antd';
import { SelectParameterDistribution } from '../../models/interfaces/distribution/inputs/select';
import { CascaderMapper } from '../../models/libraries/antd/mappers/cascaderMapper';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignCascader() {
    return (
        <AntDesignInputItem
            Distribution={SelectParameterDistribution}
            Mapper={CascaderMapper}
            hasExternalLabel={true}
        >
            {({
                disabled,
                defaultValue,
                options,
                multiple,
            }) => (
                <Cascader
                    disabled={disabled}
                    defaultValue={defaultValue}
                    multiple={multiple}
                    options={options}
                />
            )}
        </AntDesignInputItem>
    );
}