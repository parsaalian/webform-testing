import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    DiscreteValuedDistribution,
} from "../distribution";
import { InputParameterDistribution } from "./input";
import { DateTimeInputTypeEnum, IDateTimeInput } from "../../inputs/datetimeInput";

export type DateTimeInputParameterType = KeysToNewType<IDateTimeInput, any>;

export class DateTimeInputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new InputParameterDistribution();
    public parameters: DateTimeInputParameterType = {
        type: new DiscreteValuedDistribution(
            [
                DateTimeInputTypeEnum.DATE,
                DateTimeInputTypeEnum.TIME,
                DateTimeInputTypeEnum.DATETIME,
                DateTimeInputTypeEnum.WEEK,
                DateTimeInputTypeEnum.MONTH,
                DateTimeInputTypeEnum.QUARTER,
            ],
            [
                1/6,
                1/6,
                1/6,
                1/6,
                1/6,
                1/6,
            ]
        ),
        isRange: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        staticRender: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        landscape: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
    };
}