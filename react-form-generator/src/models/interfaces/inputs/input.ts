import { Nullify  } from '../../utils/modifiers';
import { ILabel } from '../primitives/label';
import { IValidation } from '../primitives/validation';
import { IPrefixSuffix } from '../primitives/prefixSuffix';

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