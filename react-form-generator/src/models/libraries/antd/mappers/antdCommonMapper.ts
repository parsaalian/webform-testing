import { Nullify } from "../../../utils/modifiers";
import { IValidation, ValidationStateEnum } from "../../../interfaces/primitives/validation";

export class AntDesignCommonMapper {
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