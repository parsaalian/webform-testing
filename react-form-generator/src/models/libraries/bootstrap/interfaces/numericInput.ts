import { LabelFloatingEnum } from "../../../componentModels/primitives/label";

export interface BootstrapNumericInput {
    label: string;
    floating: LabelFloatingEnum;
    disabled: boolean;
    isInvalid: boolean;
    isValid: boolean;
    plaintext: boolean;
    readOnly: boolean;
    value: number;
    min: number;
    max: number;
    step: number;
    validation: any;
}