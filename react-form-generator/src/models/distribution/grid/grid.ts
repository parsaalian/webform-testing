import { KeysToNewType } from "../../componentModels/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import {
    ArrayOfDistribution,
    PoissonDistribution,
} from "../distribution";
import { IGrid } from "../../componentModels/grid/grid";
import { RowParameterDistribution } from "./row";

export type GridParameterType = KeysToNewType<IGrid, any>;

export class GridParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: GridParameterType;

    constructor(cols: number) {
        super();
        this.parameters = {
            rows: new ArrayOfDistribution(
                new PoissonDistribution(5),
                new RowParameterDistribution(cols),
            ),
        }
    }
}