import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    ConstantValueDistribution,
    DiscreteValuedDistribution,
    PoissonDistribution,
    RecursiveKeyValueDistribution
} from "../distribution";
import { ISlider } from "../../inputs/slider";
import { InputParameterDistribution } from "./input";
import { InputOrientationEnum } from "../../../utils/orientation";

export type SliderParameterType = KeysToNewType<ISlider, any>;

export class SliderParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new InputParameterDistribution();
    public parameters: SliderParameterType = {
        max: new ConstantValueDistribution(100),
        min: new ConstantValueDistribution(-100),
        step: new PoissonDistribution(2),
        orientation: new DiscreteValuedDistribution(
            [InputOrientationEnum.HORIZONTAL, InputOrientationEnum.VERTICAL], [0.5, 0.5]
        ),
        marks: new RecursiveKeyValueDistribution(2, 0, 'number'),
        useMarksOnly: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        hasInputField: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        isInverted: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        hasTrack: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        isRange: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
    };
}