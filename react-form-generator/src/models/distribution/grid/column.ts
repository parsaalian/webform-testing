import { KeysToNewType } from "../../componentModels/mapper";
import { ComponentParameterDistribution } from "../componentParameterDistribution";
import { IColumn } from "../../componentModels/grid/column";
import { DiscreteValuedDistribution } from "../distribution";
import { InputTypesEnum } from "./inputTypes";

export type ColumnParameterType = KeysToNewType<IColumn, any>;

export class ColumnParameterDistribution extends ComponentParameterDistribution {
    public parentDistribution = null;
    public parameters: ColumnParameterType;

    constructor(span: number) {
        super();
        this.parameters = {
            content: new DiscreteValuedDistribution([
                InputTypesEnum.AUTOCOMPLETE,
                InputTypesEnum.CASCADER,
                InputTypesEnum.CHECKBOX,
                InputTypesEnum.DATE,
                InputTypesEnum.NUMBER,
                InputTypesEnum.RADIO,
                InputTypesEnum.RATE,
                InputTypesEnum.SELECT,
                InputTypesEnum.SLIDER,
                InputTypesEnum.SWITCH,
                InputTypesEnum.TEXT,
                InputTypesEnum.TRANSFER,
                InputTypesEnum.TREESELECT,
                InputTypesEnum.UPLOAD,
                InputTypesEnum.TEXTAREA,
            ],
            [
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
                1/15,
            ]),
            span: span,
        }
    }
}