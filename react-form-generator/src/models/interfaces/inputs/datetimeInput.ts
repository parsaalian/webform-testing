import { Nullify } from "../../utils/modifiers";
import { IInput } from "./input";

export enum DateTimeInputTypeEnum {
    DATE = "date",
    TIME = "time",
    DATETIME = "datetime",
    WEEK = "week",
    MONTH = "month",
    QUARTER = "quarter",
}

export interface IDateTimeInput extends IInput<Date | Date[]> {
    type: DateTimeInputTypeEnum;
    staticRender: Nullify<boolean>;
    landscape: Nullify<boolean>;
}