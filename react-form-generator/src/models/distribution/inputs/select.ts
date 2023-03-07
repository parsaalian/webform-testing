
import { KeysToNewType } from "../../interfaces/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    ArrayOfDistribution,
    DiscreteValuedDistribution,
    PoissonDistribution,
    RecursiveKeyValueDistribution,
} from "../distribution";
import { ISelect } from "../../interfaces/inputs/select";
import { InputParameterDistribution } from "./input";

export type SelectParameterType = KeysToNewType<ISelect, any>;

export class SelectParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new InputParameterDistribution();
    public parameters: SelectParameterType = {
        options: new RecursiveKeyValueDistribution(3, 2),
        tagLimits: new PoissonDistribution(2),
        selected: new ArrayOfDistribution(
            new PoissonDistribution(2),
            new PoissonDistribution(3),
        ),
        mode: new DiscreteValuedDistribution(['single', 'multiple' , 'tags'], [1/3, 1/3, 1/3]),
    };
}