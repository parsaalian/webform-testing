import { AntDesignDatePicker } from "../interfaces/datePicker";
import { IDateTimeInput, DateTimeInputTypeEnum } from "../../../componentModels/inputs/datetimeInput";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class DatePickerMapper extends AntDesignCommonMapper {
    public static mapValues(dateInput: IDateTimeInput): AntDesignDatePicker {
        const {
            value,
            isRange,
            type,
        } = dateInput;

        // console.log(value);

        const mappedPicker = this.mapTypeToPicker(type);
        const mappedShowTime = type === DateTimeInputTypeEnum.DATETIME;
        const mappedDefaultValue = value || new Date();
        const mappedIsRange = isRange || false;

        return {
            ...this.mapCommonValues(dateInput),
            picker: mappedPicker,
            defaultValue: mappedDefaultValue,
            isRange: mappedIsRange,
            showTime: mappedShowTime,
        }
    }

    public static mapTypeToPicker(type: DateTimeInputTypeEnum): string {
        switch (type) {
            case DateTimeInputTypeEnum.DATE:
                return 'date';
            case DateTimeInputTypeEnum.TIME:
                return 'time';
            case DateTimeInputTypeEnum.DATETIME:
                return 'date';
            case DateTimeInputTypeEnum.WEEK:
                return 'week';
            case DateTimeInputTypeEnum.MONTH:
                return 'month';
            case DateTimeInputTypeEnum.QUARTER:
                return 'quarter';
            case DateTimeInputTypeEnum.YEAR:
                return 'year';
            default:
                return 'date';
        }
    }
}