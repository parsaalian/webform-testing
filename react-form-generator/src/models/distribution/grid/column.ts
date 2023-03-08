import { KeysToNewType } from "../../componentModels/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import { IColumn } from "../../componentModels/grid/column";
import { DiscreteValuedDistribution } from "../distribution";

export type ColumnParameterType = KeysToNewType<IColumn, any>;

export class ColumnParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: ColumnParameterType;

    constructor(span: number) {
        super();
        this.parameters = {
            content: new DiscreteValuedDistribution([
                "autoComplete",
                "cascader",
                "checkbox",
                "date",
                "number",
                "radio",
                "rate",
                "select",
                "slider",
                "switch",
                "transfer",
                "treeSelect",
                "upload",
            ],
            [
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
                1/13,
            ]),
            span: span,
        }
    }
}