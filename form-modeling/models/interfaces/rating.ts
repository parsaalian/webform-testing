import { IIcon } from "./icon";
import { ISlider } from "./slider";

export interface IRating extends ISlider {
    icon: IIcon | Array<IIcon>;
}