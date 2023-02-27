import {
    Input,
    InputConstructorType
} from './inputEntity';

export type NumberInputConstructorType = InputConstructorType<number>;

export abstract class NumberInput extends Input<number> {
    constructor({
        ...inputConstructorValues
    }: NumberInputConstructorType) {
        super(inputConstructorValues);
    }
}