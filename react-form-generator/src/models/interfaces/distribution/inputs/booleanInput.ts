import { KeysToNewType } from '../../mapper';
import { ComponentParameterDistribution } from '../componentParameterDistribution';
import { ConstantValueDistribution, DiscreteValuedDistribution } from '../distribution';
import {
    IBooleanInput,
    BooleanInputEnum,
    BooleanInputStateEnum,
} from '../../inputs/booleanInput';
import { InputParameterDistribution } from './input';
import { IconParameterDistribution } from '../primitives/icon';


export type BooleanInputParameterType = KeysToNewType<IBooleanInput, any>;

export class BooleanInputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new InputParameterDistribution();
    public parameters: BooleanInputParameterType = {
        type: new DiscreteValuedDistribution(
            [BooleanInputEnum.CHECKBOX, BooleanInputEnum.SWITCH, BooleanInputEnum.SWITCH],
            [1/3, 1/3, 1/3]
        ),
        renderAs: new DiscreteValuedDistribution(
            [
                null,
                new DiscreteValuedDistribution(
                    [new IconParameterDistribution(), new IconParameterDistribution()],
                    [0.5, 0.5]
                ),
            ],
            [0.5, 0.5]
        ),
        validStates: new ConstantValueDistribution([
            BooleanInputStateEnum.CHECKED,
            BooleanInputStateEnum.UNCHECKED,
            BooleanInputStateEnum.INDETERMINATE,
        ]),
    };
}