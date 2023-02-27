import { Nullify  } from '../types/modifiers';
import { ILabel } from './label';
import { IValidation } from './validation';
import { IPrefixSuffix } from './prefixSuffix';

export interface IInput<T> {
    value: Nullify<T>;
    label: Nullify<ILabel>;
    disabled: boolean;
    readonly: boolean;
    required: boolean;
    hint: Nullify<string>;
    feedback: Nullify<string>;
    validation: Nullify<IValidation>;
    prefix: Nullify<IPrefixSuffix>;
    suffix: Nullify<IPrefixSuffix>;
    color: Nullify<string>;
    size: Nullify<string>;
}