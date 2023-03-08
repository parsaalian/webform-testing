import { Radio } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignRadio(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={false}>
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