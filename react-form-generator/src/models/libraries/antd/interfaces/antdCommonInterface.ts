import { Nullify } from "../../../utils/modifiers";

export interface AntDesignCommonInterface {
    label: Nullify<string>;
    defaultValue: Nullify<any>;
    disabled: boolean;
    required: boolean;
    validationState: string;
    validationMessage: string;
}