
import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    PoissonDistribution,
    RecursiveKeyValueDistribution,
} from "../distribution";
import { ISelect } from "../../inputs/select";
import { InputParameterDistribution } from "./input";

export type SelectParameterType = KeysToNewType<ISelect, any>;

export class SelectParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new InputParameterDistribution();
    public parameters: SelectParameterType = {
        maximumSelectionLength: new PoissonDistribution(2),
        options: new RecursiveKeyValueDistribution(3, 2),
        tagLimits: new PoissonDistribution(2),
    };
}