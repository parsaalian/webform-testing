import { AntDesignCommonInterface } from "./antdCommonInterface";

export interface AntDesignDatePicker extends AntDesignCommonInterface {
    picker: string;
    isRange: boolean;
    showTime: boolean;
}