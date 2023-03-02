import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import { RandomWordDistribution } from "../distribution";
import { IButton } from "../../primitives/button";

export type ButtonParameterType = KeysToNewType<IButton, any>;

export class ButtonParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: ButtonParameterType = {
        label: new RandomWordDistribution(1),
    };
}