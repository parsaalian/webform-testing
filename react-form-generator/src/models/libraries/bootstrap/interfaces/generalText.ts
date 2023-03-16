import { BootstrapCommonInterface } from "../commonInterface";
import { Nullify } from "../../../utils/modifiers";

export interface BootstrapGeneralTextualInput extends BootstrapCommonInterface {
    floating: boolean;
    plaintext: boolean;
    readonly: boolean;
    type: string;
    placeholder: Nullify<string>;
}