import { Nullify } from '../types/modifiers';
import { IInput } from './input';

export interface INumericInput extends IInput<number> {
    min: Nullify<number>;
    max: Nullify<number>;
    step: Nullify<number>;
}