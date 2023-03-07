import { BootstrapSelect } from "../interfaces/select";
import { ISelect } from "../../../componentModels/inputs/select";
import { ValidationStateEnum } from "../../../componentModels/primitives/validation";

export class SelectMapper {
    public static mapValues(selectInput: ISelect): BootstrapSelect {
        const {
            label,
            disabled,
            validation,
            value,
            options,
        } = selectInput;

        const mappedLabel = label && label.value ? label.value : '';
        const mappedDisabled = disabled;
        const mappedIsInvalid = (validation && validation.state === ValidationStateEnum.INVALID) || false;
        const mappedIsValid = (validation && validation.state === ValidationStateEnum.VALID) || false;
        const mappedValue = value || '';
        const mappedOptions = options.map((option) => ({
            key: option.key,
            value: option.value,
            children: null,
        })) || [];

        return {
            label: mappedLabel,
            disabled: mappedDisabled,
            isInvalid: mappedIsInvalid,
            isValid: mappedIsValid,
            value: mappedValue,
            options: mappedOptions,
        };
    }
}