import { DatePicker, TimePicker } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

// must fix date.locale error
export default function AntDesignDatePicker(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={true}>
            {({
                disabled,
                defaultValue,
                picker,
                showTime,
                isRange,
            }) => {
                let ValuePicker;

                if (picker === "time") {
                    ValuePicker = TimePicker;
                }
                else {
                    ValuePicker = DatePicker;
                }

                if (isRange) {
                    return (
                        <ValuePicker.RangePicker
                            disabled={disabled}
                            defaultValue={defaultValue}
                            picker={picker}
                            showTime={showTime}
                        />
                    );
                }
                return (
                    <ValuePicker
                        disabled={disabled}
                        defaultValue={defaultValue}
                        picker={picker}
                        showTime={showTime}
                    />
                )
            }}
        </AntDesignInputItem>
    );
}

