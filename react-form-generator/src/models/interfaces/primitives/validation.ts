import { Nullify } from "../../types/modifiers";
import { IIcon } from './icon';

export enum ValidationStateEnum {
    UNKNOWN = 'unknown',
    VALID = 'valid',
    INVALID = 'invalid',
    WARNING = 'warning',
}

export interface IValidation {
    state: ValidationStateEnum;
    message: string;
    icon: Nullify<IIcon>;
}