import random from "random";
import { KeysToNewType } from "../../componentModels/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import { ArrayOfDistribution, ConstantValueDistribution } from "../distribution";
import { IRow } from "../../componentModels/grid/row";
import { ColumnParameterDistribution } from "./column";

export type RowParameterType = KeysToNewType<IRow, any>;

export class RowParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: RowParameterType;

    constructor(cols: number) {
        super();
        const count = random.choice([1, 2]) || 1;
        this.parameters = {
            columns: new ArrayOfDistribution(
                new ConstantValueDistribution(count),
                new ColumnParameterDistribution(cols / count),
            ),
            width: cols
        }
    }
}