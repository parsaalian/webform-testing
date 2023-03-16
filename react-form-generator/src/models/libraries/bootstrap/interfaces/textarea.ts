import { BootstrapCommonInterface } from "../commonInterface";

export interface BootstrapTextAreaInput extends BootstrapCommonInterface {
    rows: number;
    floating: boolean;
    plaintext: boolean;
    readonly: boolean;
    placeholder: string;
}