import { Nullify } from "../types/modifiers";
import { IButton } from "./button";
import { IIcon } from "./icon";
import { IInput } from "./input";

export enum BooleanInputEnum {
    CHECKBOX = "checkbox",
    SWITCH = "switch",
    RADIO = "radio",
};

export enum BooleanInputStateEnum {
    CHECKED = "checked",
    UNCHECKED = "unchecked",
    INDETERMINATE = "indeterminate",
}

export interface IBooleanInput extends IInput<boolean> {
    type: BooleanInputEnum;
    renderAs: Nullify<IButton | IIcon>
    state: BooleanInputStateEnum;
    validStates: Array<BooleanInputStateEnum>;
}