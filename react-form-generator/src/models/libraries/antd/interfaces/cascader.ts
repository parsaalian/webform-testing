import { SelectOptions } from "../../../interfaces/inputs/select";
import { AntDesignCommonInterface } from "./antdCommonInterface";

export interface AntDesignCascader extends AntDesignCommonInterface {
    maxTagCount: number;
    options: SelectOptions;
    multiple: boolean;
}