// TODO: add prefix and suffix for text input
import {
    Input,
    InputConstructorType,
    NullifyType
} from './inputEntity';

export enum TextInputType {
    COLOR = 1,
    EMAIL = 2,
    PASSWORD = 3,
    SEARCH = 4,
    TEL = 5,
    TEXT = 6,
    URL = 7,
}

export type TextInputConstructorType = InputConstructorType<string> & {
    characterCounter?: boolean;
    minLength?: number;
    maxLength?: number;
    type?: TextInputType;
};

export type TextAreaInputConstructorType = TextInputConstructorType & {
    rows?: number;
};

export abstract class TextInput extends Input<string> {
    private characterCounter: boolean;
    private minLength: NullifyType<number>;
    private maxLength: NullifyType<number>;
    private type: TextInputType;

    constructor({
        characterCounter,
        minLength,
        maxLength,
        type,
        ...inputConstructorValues
    }: TextInputConstructorType) {
        super(inputConstructorValues);
        this.characterCounter = characterCounter || false;
        this.minLength = minLength || null;
        this.maxLength = maxLength || null;
        this.type = type || TextInputType.TEXT;
    }

    getCharacterCounter(): boolean {
        return this.characterCounter;
    }

    getMinLength(): NullifyType<number> {
        return this.minLength;
    }

    getMaxLength(): NullifyType<number> {
        return this.maxLength;
    }

    getType(): TextInputType {
        return this.type;
    }
}

export abstract class TextAreaInput extends TextInput {
    private rows: number;

    constructor({
        rows,
        ...textInputConstructorValues
    }: TextAreaInputConstructorType) {
        super({
            type: TextInputType.TEXT,
            ...textInputConstructorValues
        });
        this.rows = rows || 1;
    }

    getRows(): number {
        return this.rows;
    }
}