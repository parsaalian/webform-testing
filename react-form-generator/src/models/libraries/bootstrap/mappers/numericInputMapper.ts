import { BootstrapNumericInput } from "../interfaces/numericInput";
import { INumericInput } from "../../../interfaces/inputs/numericInput";
import { ValidationStateEnum } from "../../../interfaces/primitives/validation";
import { LabelFloatingEnum } from "../../../interfaces/primitives/label";

export class NumericInputMapper {
    public static mapValues(numericInput: INumericInput): BootstrapNumericInput {
        const {
            label,
            disabled,
            validation,
            readonly,
            value,
        } = numericInput;

        const mappedLabel = label && label.value ? label.value : '';
        const mappedFloating = label ? label.floating : LabelFloatingEnum.NOT_FLOATING;
        const mappedDisabled = disabled;
        const mappedIsInvalid = (validation && validation.state === ValidationStateEnum.INVALID) || false;
        const mappedIsValid = !mappedIsInvalid;
        const mappedPlaintext = readonly;
        const mappedReadOnly = readonly;
        const mappedValue = value || 0;

        return {
            label: mappedLabel,
            floating: mappedFloating,
            disabled: mappedDisabled,
            isInvalid: mappedIsInvalid,
            isValid: mappedIsValid,
            plaintext: mappedPlaintext,
            readOnly: mappedReadOnly,
            value: mappedValue,
        };
    }
}