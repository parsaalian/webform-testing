import { AntDesignCheckbox } from "../interfaces/checkbox";
import { BooleanInputStateEnum, IBooleanInput } from "../../../interfaces/inputs/booleanInput";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class CheckboxMapper extends AntDesignCommonMapper {
    public static mapValues(checkboxInput: IBooleanInput): AntDesignCheckbox {
        const {
            value,
        } = checkboxInput;

        const mappedValue = value === BooleanInputStateEnum.CHECKED ? true : false;
        const mappedIndeterminate = value === BooleanInputStateEnum.INDETERMINATE ? true : false;

        return {
            ...this.mapCommonValues(checkboxInput),
            defaultValue: mappedValue,
            indeterminate: mappedIndeterminate,
        };
    }
}