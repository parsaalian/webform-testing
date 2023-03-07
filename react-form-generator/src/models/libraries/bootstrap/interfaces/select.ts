import { SelectOptions } from "../../../componentModels/inputs/select";

export interface BootstrapSelect {
    label: string;
    disabled: boolean;
    isInvalid: boolean;
    isValid: boolean;
    value: any;
    options: SelectOptions;
}