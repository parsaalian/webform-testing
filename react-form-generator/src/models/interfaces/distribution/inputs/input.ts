import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    DiscreteValuedDistribution,
    IDistribution,
    NullDistribution,
    RandomWordDistribution
} from "../distribution";
import { IInput } from "../../inputs/input";

export type InputParameterType = KeysToNewType<IInput<any>, IDistribution<any>>;

export class InputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: InputParameterType = {
        value: new NullDistribution(),
        label: new NullDistribution(),
        disabled: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        readonly: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        required: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        hint: new RandomWordDistribution({ exactly: 1, join: " " }),
        feedback: new RandomWordDistribution({ min: 3, max: 12, join: " " }),
        validation: new NullDistribution(),
        prefix: new NullDistribution(),
        suffix: new NullDistribution(),
        color: new NullDistribution(),
        size: new NullDistribution()
    };
}