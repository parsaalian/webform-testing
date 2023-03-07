import { KeysToNewType } from "../../componentModels/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import { RandomWordDistribution } from "../distribution";
import { IButton } from "../../componentModels/primitives/button";

export type ButtonParameterType = KeysToNewType<IButton, any>;

export class ButtonParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: ButtonParameterType = {
        label: new RandomWordDistribution(1),
    };
}