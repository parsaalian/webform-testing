import { Nullify } from "../../utils/modifiers";
import { IValidation, ValidationStateEnum } from "../../componentModels/primitives/validation";
import { IInput } from "../../componentModels/inputs/input";
import { BootstrapCommonInterface } from "./commonInterface";

export class BootstrapCommonMapper {
    protected static mapCommonValues(input: IInput<any>): BootstrapCommonInterface {
        const {
            label,
            value,
            disabled,
            validation,
        } = input;

        const mappedLabel = label && label.value ? label.value : null;
        const mappedDefaultValue = value || null;
        const mappedDisabled = disabled || false;
        const {
            validationState,
            validationMessage,
        } = this.mapValidation(validation);
        const mappedIsValid = validationState === 'valid';
        const mappedIsInvalid = validationState === 'invalid';

        return {
            label: mappedLabel,
            defaultValue: mappedDefaultValue,
            disabled: mappedDisabled,
            isValid: mappedIsValid,
            isInvalid: mappedIsInvalid,
            validationState,
            validationMessage,
        }
    }

    protected static mapValidation(validation: Nullify<IValidation>): { validationState: string, validationMessage: string } {
        let validationState: string = '', validationMessage: string = '';
        if (validation !== null) {
            const { state, message } = validation;

            validationMessage = message;
            if (state === ValidationStateEnum.INVALID) {
                validationState = 'invalid';
            }
            else if (state === ValidationStateEnum.VALID) {
                validationState = 'valid';
            }
        }

        return {
            validationState,
            validationMessage,
        }
    }
}