import { BootstrapTextAreaInput } from "../interfaces/textareaInput";
import { ITextAreaInput } from "../../../interfaces/inputs/textareaInput";
import { ValidationStateEnum } from "../../../interfaces/primitives/validation";
import { LabelFloatingEnum } from "../../../interfaces/primitives/label";

export class TextAreaInputMapper {
    public static mapValues(textAreaInput: ITextAreaInput): BootstrapTextAreaInput {
        const {
            label,
            disabled,
            validation,
            readonly,
            rows,
            hint,
            value,
        } = textAreaInput;

        const mappedLabel = label && label.value ? label.value : '';
        const mappedFloating = label ? label.floating : LabelFloatingEnum.NOT_FLOATING;
        const mappedDisabled = disabled;
        const mappedIsInvalid = (validation && validation.state === ValidationStateEnum.INVALID) || false;
        const mappedIsValid = (validation && validation.state === ValidationStateEnum.VALID) || false;
        const mappedPlaintext = readonly;
        const mappedReadOnly = readonly;
        const mappedRows = rows || 1;
        const mappedValue = value || '';
        const mappedPlaceholder = hint || '';

        return {
            label: mappedLabel,
            floating: mappedFloating,
            disabled: mappedDisabled,
            isInvalid: mappedIsInvalid,
            isValid: mappedIsValid,
            plaintext: mappedPlaintext,
            readOnly: mappedReadOnly,
            rows: mappedRows,
            value: mappedValue,
            placeholder: mappedPlaceholder,
            validation,
        };
    }
}