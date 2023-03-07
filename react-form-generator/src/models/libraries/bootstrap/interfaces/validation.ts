import { ValidationStateEnum } from '../../../componentModels/primitives/validation'

export interface BootstrapValidation {
    state: ValidationStateEnum;
    message: string;
}