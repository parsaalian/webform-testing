import { Nullify } from "./modifiers";
import {
    IGeneralTextualInput,
    TextualInputTypeEnum
} from "../componentModels/inputs/generalTextualInput";
import { RegexPatternGenerator } from "./regexPatternGenerator";
import { ILabel } from "../componentModels/primitives/label";
import { IValidation } from "../componentModels/primitives/validation";
import { IPrefixSuffix } from "../componentModels/primitives/prefixSuffix";

export abstract class GeneralTextualInput implements IGeneralTextualInput {
    public type: TextualInputTypeEnum;
    public regex: RegExp;
    public minChars: number;
    public maxChars: number;
    public characterCounter: boolean;
    public value: Nullify<string>;
    public label: Nullify<ILabel>;
    public readonly: boolean;
    public disabled: boolean;
    public required: boolean;
    public hint: Nullify<string>;
    public feedback: Nullify<string>;
    public validation: Nullify<IValidation>;
    public prefix: Nullify<IPrefixSuffix>;
    public suffix: Nullify<IPrefixSuffix>;
    public color: Nullify<string>;
    public size: Nullify<string>;

    constructor({
        type,
        minChars,
        maxChars,
        characterCounter,
        label,
        value,
        readonly,
        disabled,
        required,
        hint,
        feedback,
        validation,
        prefix,
        suffix,
        color,
        size,
    }: IGeneralTextualInput) {
        this.type = type;
        this.minChars = minChars || -1;
        this.maxChars = maxChars || -1;
        this.characterCounter = characterCounter || false;
        this.regex = this.generateRegexFromType();
        this.value = value || '';
        this.label = label || null;
        this.readonly = readonly || false;
        this.disabled = disabled || false;
        this.required = required || false;
        this.hint = hint || null;
        this.feedback = feedback || null;
        this.validation = validation || null;
        this.prefix = prefix || null;
        this.suffix = suffix || null;
        this.color = color || null;
        this.size = size || null;
        this.color = color || null;
    }

    private generateRegexFromType(): RegExp {
        return RegexPatternGenerator.generateRegexFromType(this.type);
    }
}