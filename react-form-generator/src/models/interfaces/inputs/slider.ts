import { IInput } from "./input";
import { InputOrientationEnum } from "../../utils/orientation";
import { ILabel } from "../primitives/label";

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