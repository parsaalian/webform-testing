import {
    Input,
    InputConstructorType,
    NullifyType,
} from './inputEntity';

export type Option<T> = {
    value: string;
    label: T;
};

export type Options<T> = Array<Option<T>>;

export type SelectInputConstructorType<T> = InputConstructorType<T> & {
    selected?: Option<T>;
    options?: Options<T>;
};

export abstract class SelectInput<T> extends Input<T> {
    private options: Options<T>;
    private selected: NullifyType<Option<T>>;

    constructor({
        options,
        selected,
        ...inputConstructorValues
    }: SelectInputConstructorType<T>) {
        super(inputConstructorValues);
        this.options = options || [];
        this.selected = selected || null;
    }

    getOptions(): Options<T> {
        return this.options;
    }

    getSelected(): NullifyType<Option<T>> {
        return this.selected;
    }
}

// export abstract class MultipleSelectInput<T> extends SelectInput<T> {};
// export abstract class TreeSelectInput<T> extends SelectInput<T> {};