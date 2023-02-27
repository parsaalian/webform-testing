import { Validation } from './validationEntity';

export type InputConstructorType<T> = {
    label?: string;
    defaultValue?: T;
    disabled?: boolean;
    readonly?: boolean;
    required?: boolean;
    helper?: string;
    placeholder?: T;
    validation?: Validation;
};

export type NullifyType<T> = T | null;

export abstract class InputEntity<T> {
    private readonly label: NullifyType<string>;
    private readonly defaultValue: NullifyType<T>;
    private readonly disabled: boolean;
    private readonly readonly: boolean;
    private readonly required: boolean;
    private readonly helper: NullifyType<string>;
    private readonly placeholder: NullifyType<T>;
    private readonly validation: NullifyType<Validation>;

    constructor({
        label,
        defaultValue,
        disabled,
        readonly,
        required,
        helper,
        placeholder,
        validation,
    }: InputConstructorType<T>) {
        this.label = label || null;
        this.defaultValue = defaultValue || null;
        this.disabled = disabled || false;
        this.readonly = readonly || false;
        this.required = required || false;
        this.helper = helper || null;
        this.placeholder = placeholder || null;
        this.validation = validation || null;
    }

    abstract getValuesJson(): string;

    getLabel(): string | null {
        return this.label;
    }

    getDefaultValue(): NullifyType<T> {
        return this.defaultValue;
    }

    getDisabled(): boolean {
        return this.disabled;
    }

    getReadonly(): boolean {
        return this.readonly;
    }

    getRequired(): boolean {
        return this.required;
    }

    getHelper(): NullifyType<string> {
        return this.helper;
    }

    getPlaceholder(): NullifyType<T> {
        return this.placeholder;
    }

    getValidation(): NullifyType<Validation> {
        return this.validation;
    }
}
