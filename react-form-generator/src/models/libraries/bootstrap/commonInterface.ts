import { Nullify } from "../../utils/modifiers";

export interface BootstrapCommonInterface {
    label: Nullify<string>;
    defaultValue: Nullify<any>;
    disabled: boolean;
    isValid: boolean;
    isInvalid: boolean;
    validationState: string;
    validationMessage: string;
}