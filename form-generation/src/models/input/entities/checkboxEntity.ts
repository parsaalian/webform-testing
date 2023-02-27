import { InputEntity, InputConstructorType, NullifyType } from './inputEntity';
import { Icon } from './iconEntity';

export enum CheckboxBooleanState {
    UNCHECKED = 0,
    CHECKED = 1,
}

export enum CheckboxState {
    UNCHECKED = 0,
    CHECKED = 1,
    INDETERMINATE = 2,
}

export enum CheckboxGroupDirection {
    HORIZONTAL = 0,
    VERTICAL = 1,
}

export type CheckboxConstructorType<T> = InputConstructorType<T> & {
    icon?: Icon,
};

export abstract class CheckboxEntity<T> extends InputEntity<T> {
    private readonly icon: NullifyType<Icon>;

    constructor({
        icon,
        ...inputConstructorValues
    }: CheckboxConstructorType<T>) {
        super(inputConstructorValues);
        this.icon = icon || null;
    }

    getIcon(): NullifyType<Icon> {
        return this.icon;
    }
}

export abstract class BinaryCheckboxEntity extends CheckboxEntity<CheckboxBooleanState> {
    constructor(inputConstructorValues: CheckboxConstructorType<CheckboxBooleanState>) {
        super(inputConstructorValues);
    }
};

export abstract class IndeterminateCheckboxEntity extends CheckboxEntity<CheckboxState> {
    constructor(inputConstructorValues: CheckboxConstructorType<CheckboxState>) {
        super(inputConstructorValues);
    }
};

export abstract class CheckboxGroupEntity {
    private readonly checkboxes: BinaryCheckboxEntity[];
    private readonly direction: CheckboxGroupDirection;

    constructor(checkboxes: BinaryCheckboxEntity[], direction: CheckboxGroupDirection) {
        this.checkboxes = checkboxes;
        this.direction = direction;
    }

    getCheckboxes(): BinaryCheckboxEntity[] {
        return this.checkboxes;
    }

    getDirection(): CheckboxGroupDirection {
        return this.direction;
    }
}

export abstract class IndeterminateCheckboxGroupEntity {
    private readonly checkboxGroup: CheckboxGroupEntity;
    private readonly indeterminateCheckbox: IndeterminateCheckboxEntity;

    constructor(checkboxGroup: CheckboxGroupEntity, indeterminateCheckbox: IndeterminateCheckboxEntity) {
        this.checkboxGroup = checkboxGroup;
        this.indeterminateCheckbox = indeterminateCheckbox;
    }

    getCheckboxGroup(): CheckboxGroupEntity {
        return this.checkboxGroup;
    }

    getIndeterminateCheckbox(): IndeterminateCheckboxEntity {
        return this.indeterminateCheckbox;
    }
}