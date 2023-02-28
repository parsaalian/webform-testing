import { IInput } from './input';

export type SimpleSelectOption = Array<{
    key: string,
    value: string,
}>

export type TreeSelectOption = Array<{
    key: string,
    value: string,
    children: Array<SimpleSelectOption | TreeSelectOption>
}>

export type SelectOptions = SimpleSelectOption |
    TreeSelectOption |
    Array<SimpleSelectOption> |
    Array<TreeSelectOption>;

export interface ISelect extends IInput<any> {
    maximumSelectionLength: number;
    tagLimits: number;
    selected: SelectOptions;
    options: SelectOptions;
}