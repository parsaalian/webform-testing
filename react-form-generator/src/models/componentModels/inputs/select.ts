import { Nullify } from '../../utils/modifiers';
import { IInput } from './input';

export type SimpleSelectOption = Array<{
    key: string,
    value: string,
    children: Nullify<Array<SimpleSelectOption>>
}>

export type SelectOptions = SimpleSelectOption | Array<SimpleSelectOption>;

export interface ISelect extends IInput<any> {
    tagLimits: number;
    selected: Array<number>;
    options: SelectOptions;
    mode: string;
}