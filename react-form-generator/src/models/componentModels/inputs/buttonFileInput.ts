import { IFileInput } from "./fileInput";
import { IButton } from "../primitives/button";

export interface IButtonFileInput extends IFileInput {
    button: IButton;
}