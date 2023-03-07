import { Nullify } from "../../../utils/modifiers";
import { IValidation, ValidationStateEnum } from "../../../componentModels/primitives/validation";
import { IInput } from "../../../componentModels/inputs/input";
import { AntDesignCommonInterface } from "../interfaces/antdCommonInterface";

export class AntDesignCommonMapper {
    protected static mapCommonValues(input: IInput<any>): AntDesignCommonInterface {
        const {
            label,
            disabled,
            required,
            validation,
            value,
        } = input;

        const mappedLabel = label && label.value ? label.value : null;
        const mappedDisabled = disabled || false;
        const mappedRequired = required || false;
        const mappedDefaultValue = value || null;
        const {
            validationState,
            validationMessage,
        } = this.mapValidation(validation);

        return {
            label: mappedLabel,
            disabled: mappedDisabled,
            required: mappedRequired,
            defaultValue: mappedDefaultValue,
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
                validationState = 'error';
            }
            else if (state === ValidationStateEnum.WARNING) {
                validationState = 'warning';
            }
            else if (state === ValidationStateEnum.VALID) {
                validationState = 'success';
            }
        }

        return {
            validationState: validationState,
            validationMessage: validationMessage,
        };
    }
}