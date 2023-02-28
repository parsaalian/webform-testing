import { Nullify } from "../../types/modifiers";
import { IInput } from "./input";

export interface ITextualInput extends IInput<string> {
    characterCounter: boolean;
    minChars: Nullify<number>;
    maxChars: Nullify<number>;
}

export interface ISearchInput extends ITextualInput {}