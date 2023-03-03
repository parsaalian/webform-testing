import { AntDesignCheckbox } from "../interfaces/checkbox";
import { BooleanInputStateEnum, IBooleanInput } from "../../../interfaces/inputs/booleanInput";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class CheckboxMapper extends AntDesignCommonMapper {
    public static mapValues(checkboxInput: IBooleanInput): AntDesignCheckbox {
        const {
            label,
            disabled,
            value,
            required,
            validation,
        } = checkboxInput;

        const mappedLabel = label && label.value ? label.value : '';
        const mappedDisabled = disabled || false;
        const mappedRequired = required || false;
        const mappedValue = value === BooleanInputStateEnum.CHECKED ? true : false;
        const mappedIndeterminate = value === BooleanInputStateEnum.INDETERMINATE ? true : false;
        const {
            validationState,
            validationMessage,
        } = this.mapValidation(validation);

        return {
            label: mappedLabel,
            disabled: mappedDisabled,
            defaultChecked: mappedValue,
            indeterminate: mappedIndeterminate,
            required: mappedRequired,
            validationState,
            validationMessage,
        };
    }
}