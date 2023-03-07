import { AntDesignCommonInterface } from "./antdCommonInterface";
import { SelectOptions } from "../../../componentModels/inputs/select";

export interface AntDesignSelect extends AntDesignCommonInterface {
    maxTagCount: number;
    options: SelectOptions;
    mode: string;
}