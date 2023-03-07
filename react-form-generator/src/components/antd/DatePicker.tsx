import { DatePicker } from 'antd';
import { DateTimeInputParameterDistribution } from '../../models/interfaces/distribution/inputs/dateInput';
import { DatePickerMapper } from '../../models/libraries/antd/mappers/datePickerMapper';
import AntDesignInputItem from './AntDesignInputItem';

const { RangePicker } = DatePicker;

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
                if (isRange) {
                    return (
                        <RangePicker
                            disabled={disabled}
                            defaultValue={defaultValue}
                            picker={picker}
                            showTime={showTime}
                        />
                    );
                }
                return (
                    <DatePicker
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

