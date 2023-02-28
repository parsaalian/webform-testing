import { IIcon } from "./icon";

export interface IButton {
    label: string | IIcon | Array<string | IIcon>;
}