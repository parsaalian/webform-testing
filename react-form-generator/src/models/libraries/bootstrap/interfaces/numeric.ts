import { BootstrapCommonInterface } from "../commonInterface";

export interface BootstrapNumericInput extends BootstrapCommonInterface {
    floating: boolean;
    plaintext: boolean;
    readonly: boolean;
    min: number;
    max: number;
    step: number;
}