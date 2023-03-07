import { KeysToNewType } from "../../interfaces/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    IDistribution,
    PoissonDistribution,
    RandomWordDistribution,
} from "../distribution";
import { TextualInputParameterDistribution } from "./textualInput";
import { ITextAreaInput } from "../../interfaces/inputs/textareaInput";

export type TextAreaInputParameterType = KeysToNewType<ITextAreaInput, IDistribution<any>>;

export class TextAreaInputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new TextualInputParameterDistribution();
    public parameters: TextAreaInputParameterType = {
        value: new RandomWordDistribution({ min: 3, max: 15, join: ' ' }),
        rows: new PoissonDistribution(3),
        minRows: new PoissonDistribution(1),
        maxRows: new PoissonDistribution(5),
    };
}

