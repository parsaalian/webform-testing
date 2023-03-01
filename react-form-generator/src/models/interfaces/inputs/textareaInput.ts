import { Nullify } from "../../utils/modifiers";
import { ITextualInput } from "./textualInput";

export interface ITextAreaInput extends ITextualInput {
    rows: Nullify<number>;
    minRows: Nullify<number>;
    maxRows: Nullify<number>;
}