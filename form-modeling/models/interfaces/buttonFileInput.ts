import { IFileInput } from "./fileInput";
import { IButton } from "./button";

export interface IButtonFileInput extends IFileInput {
    button: IButton;
}