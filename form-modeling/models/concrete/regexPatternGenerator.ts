import { IRegexPatternStorage } from "../interfaces/regexPatternStorage";
import { TextualInputTypeEnum } from "../interfaces/generalTextualInput";

export const RegexPatternStorage: IRegexPatternStorage = {
    "color": /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/,
    "email": /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
    "tel": /^(\+?1\s?)?(\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$/,
    "text": /^[\w\s]+$/,
    "url": /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/,
}

export class RegexPatternGenerator {

    public generateRegexFromType = (type: TextualInputTypeEnum): RegExp => {
        switch (type) {
            case TextualInputTypeEnum.COLOR:
                return RegexPatternStorage.color;
            case TextualInputTypeEnum.EMAIL:
                return RegexPatternStorage.email;
            case TextualInputTypeEnum.PASSWORD:
                return RegexPatternStorage.text;
            case TextualInputTypeEnum.TEL:
                return RegexPatternStorage.tel;
            case TextualInputTypeEnum.TEXT:
                return RegexPatternStorage.text;
            case TextualInputTypeEnum.SEARCH:
                return RegexPatternStorage.text;
            case TextualInputTypeEnum.URL:
                return RegexPatternStorage.url;
            default:
                return RegexPatternStorage.text;
        }
    }
}