import { KeysToNewType } from "../../interfaces/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    IDistribution,
    UniformDistribution,
    PoissonDistribution,
    ConstantValueDistribution,
} from "../distribution";
import { InputParameterDistribution } from "./input";
import { INumericInput } from "../../interfaces/inputs/numericInput";

export type NumericInputParameterType = KeysToNewType<INumericInput, IDistribution<any>>;

export class NumericInputParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = new InputParameterDistribution();
    public parameters: NumericInputParameterType = {
        value: new UniformDistribution(-100, 100),
        min: new ConstantValueDistribution(-100),
        max: new ConstantValueDistribution(100),
        step: new PoissonDistribution(2),
    };
}