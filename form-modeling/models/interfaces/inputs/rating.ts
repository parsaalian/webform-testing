import { IIcon } from "../primitives/icon";
import { ISlider } from "./slider";

export interface IRating extends ISlider {
    icon: IIcon | Array<IIcon>;
}