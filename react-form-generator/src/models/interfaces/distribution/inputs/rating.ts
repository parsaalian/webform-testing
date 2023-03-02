import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import { ConstantValueDistribution } from "../distribution";
import { IRating } from "../../inputs/rating";
import { SliderParameterDistribution } from "./slider";

export type RatingParameterType = KeysToNewType<IRating, any>;

export class RatingParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new SliderParameterDistribution();
    public parameters: RatingParameterType = {
        icon: new ConstantValueDistribution({
            name: "star",
            color: "yellow",
            size: 24,
        }),
    };
}