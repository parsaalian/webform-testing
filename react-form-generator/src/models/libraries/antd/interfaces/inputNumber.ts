import { AntDesignCommonInterface } from "./antdCommonInterface";

export interface AntDesignInputNumber extends AntDesignCommonInterface {
    min: number;
    max: number;
    step: number;
}