import { Cascader } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignCascader(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={true}>
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