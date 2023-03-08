import { Select } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignSelect(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={true}>
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