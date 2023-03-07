import { LabelFloatingEnum } from "../../../componentModels/primitives/label";

export interface BootstrapTextAreaInput {
    rows: number;
    label: string;
    floating: LabelFloatingEnum;
    disabled: boolean;
    isInvalid: boolean;
    isValid: boolean;
    plaintext: boolean;
    readOnly: boolean;
    validation: any;
    value: string;
    placeholder: string;
}