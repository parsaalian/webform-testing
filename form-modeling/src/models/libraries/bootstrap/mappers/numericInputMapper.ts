import { BootstrapNumericInput } from "../interfaces/numericInput";
import { INumericInput } from "../../../interfaces/inputs/numericInput";
import { ValidationStateEnum } from "../../../interfaces/primitives/validation";

export class NumericInputMapper {
    public static mapValues(numericInput: INumericInput): BootstrapNumericInput {
        const {
            label,
            disabled,
            validation,
            readonly,
            value,
        } = numericInput;

        const mappedLabel = label ? label.value : '';
        const mappedDisabled = disabled;
        const mappedIsInvalid = validation && validation.state === ValidationStateEnum.INVALID || false;
        const mappedIsValid = !mappedIsInvalid;
        const mappedPlaintext = readonly;
        const mappedReadOnly = readonly;
        const mappedValue = value || 0;

        return {
            label: mappedLabel,
            disabled: mappedDisabled,
            isInvalid: mappedIsInvalid,
            isValid: mappedIsValid,
            plaintext: mappedPlaintext,
            readOnly: mappedReadOnly,
            value: mappedValue,
        };
    }
}