import { Nullify } from "../../utils/modifiers";
import { IButton } from "../primitives/button";
import { IIcon } from "../primitives/icon";
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

export interface IBooleanInput extends IInput<BooleanInputStateEnum> {
    type: BooleanInputEnum;
    renderAs: Nullify<IButton | IIcon>
    validStates: Array<BooleanInputStateEnum>;
}