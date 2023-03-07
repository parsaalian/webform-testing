import { Nullify } from "../../../utils/modifiers";
import { AntDesignCommonInterface } from "./antdCommonInterface";

export interface AntDesignSwitch extends AntDesignCommonInterface {
    text: Nullify<string>;
}