import { IInput } from "../inputs/input";

export interface IColumn {
    content: IInput<any>;
    span: number;
}