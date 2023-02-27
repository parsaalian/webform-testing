import { ITextualInput } from "./textualInput";

export enum TextualInputTypeEnum {
    COLOR = "color",
    EMAIL = "email",
    PASSWORD = "password",
    TEXT = "text",
    SEARCH = "search",
    URL = "url",
    TEL = "tel",
}

export interface IGeneralTextualInput extends ITextualInput {
    type: TextualInputTypeEnum;
    regex: RegExp;
}