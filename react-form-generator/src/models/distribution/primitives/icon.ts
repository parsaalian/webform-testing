import { KeysToNewType } from "../../componentModels/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import { ConstantValueDistribution, NullDistribution } from "../distribution";
import { IIcon } from "../../componentModels/primitives/icon";

export type IconParameterType = KeysToNewType<IIcon, any>;

export class IconParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: IconParameterType = {
        name: new ConstantValueDistribution('star'),
        color: new ConstantValueDistribution('red'),
        size: new ConstantValueDistribution('large'),
        component: new NullDistribution(),
    };
}