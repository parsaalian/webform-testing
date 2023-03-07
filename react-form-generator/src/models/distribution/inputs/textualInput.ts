import { KeysToNewType } from "../../interfaces/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    IDistribution,
    PoissonDistribution,
    DiscreteValuedDistribution
} from "../distribution";
import { InputParameterDistribution } from "./input";
import { ITextualInput } from "../../interfaces/inputs/textualInput";

export type TextualInputParameterType = KeysToNewType<ITextualInput, IDistribution<any>>;

export class TextualInputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new InputParameterDistribution();
    public parameters: TextualInputParameterType = {
        characterCounter: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        minChars: new PoissonDistribution(1),
        maxChars: new PoissonDistribution(10),
    };
}