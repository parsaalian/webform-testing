import { AutoComplete } from 'antd';
import { SelectParameterDistribution } from '../../models/distribution/inputs/select';
import { AutoCompleteMapper } from '../../models/libraries/antd/mappers/autoCompleteMapper';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignAutoComplete() {
    return (
        <AntDesignInputItem
            Distribution={SelectParameterDistribution}
            Mapper={AutoCompleteMapper}
            hasExternalLabel={true}
        >
            {({
                disabled,
                defaultValue,
                options,
            }) => (
                <AutoComplete
                    disabled={disabled}
                    defaultValue={defaultValue}
                    options={options}
                />
            )}
        </AntDesignInputItem>
    );
}