import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    IDistribution,
    DiscreteValuedDistribution,
} from "../distribution";
import { TextualInputParameterDistribution } from "./textualInput";
import {
    IGeneralTextualInput,
    TextualInputTypeEnum
} from "../../inputs/generalTextualInput";

export type GeneralTextualInputParameterType = KeysToNewType<IGeneralTextualInput, IDistribution<any>>;

export class GeneralTextualInputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new TextualInputParameterDistribution();
    public parameters: GeneralTextualInputParameterType = {
        type: new DiscreteValuedDistribution([
            TextualInputTypeEnum.COLOR,
            TextualInputTypeEnum.EMAIL,
            TextualInputTypeEnum.PASSWORD,
            TextualInputTypeEnum.TEL,
            TextualInputTypeEnum.TEXT,
            TextualInputTypeEnum.SEARCH,
            TextualInputTypeEnum.URL,
        ], [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]),
    };
}