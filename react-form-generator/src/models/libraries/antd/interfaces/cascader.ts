import { SelectOptions } from "../../../interfaces/inputs/select";

export interface AntDesignCascader {
    label: string;
    defaultValue: SelectOptions;
    disabled: boolean;
    required: boolean;
    maxTagCount: number;
    options: SelectOptions;
    validationState: string;
    validationMessage: string;
    multiple: boolean;
}