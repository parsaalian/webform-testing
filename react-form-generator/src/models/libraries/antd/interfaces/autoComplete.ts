import { SelectOptions } from "../../../componentModels/inputs/select";
import { AntDesignCommonInterface } from "./antdCommonInterface";

export interface AntDesignAutoComplete extends AntDesignCommonInterface {
    options: SelectOptions;
}