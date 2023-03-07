import { DatePicker, TimePicker } from 'antd';
import { DateTimeInputParameterDistribution } from '../../models/distribution/inputs/dateInput';
import { DatePickerMapper } from '../../models/libraries/antd/mappers/datePickerMapper';
import AntDesignInputItem from './AntDesignInputItem';

// must fix date.locale error
export default function AntDesignDatePicker() {
    return (
        <AntDesignInputItem
            Distribution={DateTimeInputParameterDistribution}
            Mapper={DatePickerMapper}
            hasExternalLabel={true}
        >
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

