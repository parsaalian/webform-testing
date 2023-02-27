import { IInput } from "./input";
import { IButton } from "./button";
import { IIcon } from "./icon";

export interface IPrefixSuffix {
    renderAs: IIcon | IButton | IInput<any> | string;
}