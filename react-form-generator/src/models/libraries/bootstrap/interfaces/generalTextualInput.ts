import { LabelFloatingEnum } from "../../../componentModels/primitives/label";

export interface BootstrapGeneralTextualInput {
    label: string;
    floating: LabelFloatingEnum;
    disabled: boolean;
    isInvalid: boolean;
    isValid: boolean;
    plaintext: boolean;
    readOnly: boolean;
    type: string;
    validation: any;
    value: string;
    placeholder: string;
}