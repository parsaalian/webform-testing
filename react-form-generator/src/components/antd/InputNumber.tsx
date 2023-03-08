import { InputNumber } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignInputNumber(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={true}>
            {({
                disabled,
                defaultValue,
                min,
                max,
                step,
            }) => (
                <InputNumber
                    disabled={disabled}
                    defaultValue={defaultValue}
                    min={min}
                    max={max}
                    step={step}
                />
            )}
        </AntDesignInputItem>
    );
}