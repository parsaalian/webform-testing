import { ComponentParameterDistribution } from "../componentParameterDistribution";
import { InputParameterDistribution } from "./input";

export class TextualInputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new InputParameterDistribution();
    public parameters: any = {};
}