import { BootstrapValidation } from "../interfaces/validation";
import { IValidation } from "../../../interfaces/primitives/validation";
import { ValidationStateEnum } from "../../../interfaces/primitives/validation";

export class ValidationMapper {
    public static mapValues(validation: IValidation): BootstrapValidation {
        const {
            state,
            message
        } = validation;
        
        let mappedState = state;
        if (state === ValidationStateEnum.WARNING) {
            mappedState = ValidationStateEnum.UNKNOWN;
        }

        return {
            state: mappedState,
            message,
        }
    }
}