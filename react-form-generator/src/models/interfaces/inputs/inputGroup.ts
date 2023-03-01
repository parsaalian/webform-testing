import { IInput } from "./input";

export interface IInputGroup extends IInput<any> {
    inputs: IInput<any>[];
}