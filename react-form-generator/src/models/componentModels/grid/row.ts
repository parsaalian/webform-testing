import { IColumn } from './column';

export interface IRow {
    columns: Array<IColumn>;
    width: number;
}