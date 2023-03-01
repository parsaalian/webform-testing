import { KeysToNewType } from "../../mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    IDistribution,
    RandomWordDistribution,
    DiscreteValuedDistribution,
    NullDistribution
} from '../distribution';
import { IValidation, ValidationStateEnum } from "../../primitives/validation";

export type ValidationParameterType = KeysToNewType<IValidation, IDistribution<any>>;

export class ValidationParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: ValidationParameterType = {
        state: new DiscreteValuedDistribution(
            [ValidationStateEnum.UNKNOWN, ValidationStateEnum.VALID, ValidationStateEnum.INVALID, ValidationStateEnum.WARNING],
            [0.25, 0.25, 0.25, 0.25]
        ),
        message: new RandomWordDistribution({ min: 3, max: 10, join: " " }),
        icon: new NullDistribution(),
    }
}