import { ValidationStateEnum } from '../../../interfaces/primitives/validation'

export interface BootstrapValidation {
    state: ValidationStateEnum;
    message: string;
}