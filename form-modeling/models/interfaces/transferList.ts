import { IBooleanInputGroup } from "./booleanInputGroup";
import { ISearchInput } from "./textualInput";

export interface ITransferList {
    source: IBooleanInputGroup,
    target: IBooleanInputGroup,
    sourceSearch: ISearchInput,
    targetSearch: ISearchInput,
}