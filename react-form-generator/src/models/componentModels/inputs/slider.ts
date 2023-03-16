import { IInput } from "./input";
import { InputOrientationEnum } from "../../utils/orientation";

export interface ISlider extends IInput<number | number[]> {
    min: number;
    max: number;
    step: number;
    marks: Array<{ label: any, value: number }> | boolean;
    hasInputField: boolean;
    isInverted: boolean;
    hasTrack: boolean;
    orientation: InputOrientationEnum;
    isRange: boolean;
    useMarksOnly: boolean;
}