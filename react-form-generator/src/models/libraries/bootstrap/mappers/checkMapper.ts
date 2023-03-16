import { BootstrapCheck } from "../interfaces/check";
import { BooleanInputStateEnum, IBooleanInput } from "../../../componentModels/inputs/booleanInput";
import { BootstrapCommonMapper } from "../commonMapper";

export class CheckMapper extends BootstrapCommonMapper {
    public static mapValues(checkboxInput: IBooleanInput): BootstrapCheck {
        const {
            value,
        } = checkboxInput;

        const mappedValue = value === BooleanInputStateEnum.CHECKED ? true : false;

        return {
            ...this.mapCommonValues(checkboxInput),
            defaultValue: mappedValue,
        };
    }
}
