import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    IDistribution,
    RandomWordDistribution,
    DiscreteValuedDistribution
} from '../distribution';
import { ILabel } from "../../primitives/label";

export type LabelParameterType = KeysToNewType<ILabel, IDistribution<any>>;

export class LabelParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: LabelParameterType = {
        value: new RandomWordDistribution({ min: 1, max: 3, join: " " }),
        placement: new DiscreteValuedDistribution(["top", "bottom", "left", "right"], [0.25, 0.25, 0.25, 0.25]),
        floating: new DiscreteValuedDistribution(["floating", "not-floating"], [0.5, 0.5])
    }
}