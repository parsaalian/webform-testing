import { IInput } from "./input";
import { InputOrientationEnum } from "../types/orientation";
import { ILabel } from "./label";

export interface ISlider extends IInput<number | number[]> {
    min: number;
    max: number;
    step: number;
    marks: Array<{ label: ILabel, value: number }> | boolean;
    hasInputField: boolean;
    isInverted: boolean;
    hasTrack: boolean;
    orientation: InputOrientationEnum;
}