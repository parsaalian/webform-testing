import { AutoComplete } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignAutoComplete(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={true}>
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