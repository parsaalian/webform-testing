import { IButton } from "../../../interfaces/primitives/button";
import { Nullify } from "../../../utils/modifiers";
import { AntDesignCommonInterface } from "./antdCommonInterface";

export interface AntDesignRadio extends AntDesignCommonInterface {
    renderAs: Nullify<IButton>;
}