import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    DiscreteValuedDistribution,
    NullDistribution,
    RandomWordDistribution
} from "../distribution";
import { IInput } from "../../inputs/input";
import { LabelParameterDistribution } from "../primitives/label";
import { ValidationParameterDistribution } from "../primitives/validation";

export type InputParameterType = KeysToNewType<IInput<any>, any>;

export class InputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: InputParameterType = {
        value: new NullDistribution(),
        label: new LabelParameterDistribution(),
        disabled: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        readonly: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        required: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        hint: new RandomWordDistribution({ exactly: 1, join: " " }),
        feedback: new RandomWordDistribution({ min: 3, max: 12, join: " " }),
        validation: new ValidationParameterDistribution(),
        prefix: new NullDistribution(),
        suffix: new NullDistribution(),
        color: new NullDistribution(),
        size: new NullDistribution()
    };
}