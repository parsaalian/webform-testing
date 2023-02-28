import { Nullify } from "../../types/modifiers";
import { InputOrientationEnum } from "../../types/orientation";
import {
    IBooleanInput,
    BooleanInputStateEnum
} from "../inputs/booleanInput";
import { ILabel } from "../primitives/label";

export interface IBooleanInputGroup {
    label: Nullify<ILabel>;
    inputs: Array<IBooleanInput>;
    maxChecked: Nullify<number>;
    aggregatedState: Nullify<BooleanInputStateEnum>;
    aggregatedDisplayer: Nullify<IBooleanInput>;
    orientation: InputOrientationEnum;
}