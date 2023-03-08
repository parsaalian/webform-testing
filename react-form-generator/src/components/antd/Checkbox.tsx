import { Checkbox } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignCheckbox(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={false}>
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