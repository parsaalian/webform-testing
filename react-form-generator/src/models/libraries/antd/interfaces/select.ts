import { SelectOptions } from "../../../interfaces/inputs/select";

export interface AntDesignSelect {
    label: string;
    defaultValue: SelectOptions;
    disabled: boolean;
    required: boolean;
    maxTagCount: number;
    options: SelectOptions;
    validationState: string;
    validationMessage: string;
    mode: string;
}