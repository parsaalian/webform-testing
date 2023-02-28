import { ISelect } from "./select";
import { ISearchInput } from "./textualInput";

export interface ISelectSearchInput extends ISearchInput {
    select: ISelect;
};