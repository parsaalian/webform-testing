import { AntDesignCommonInterface } from "./antdCommonInterface";

export interface AntDesignSlider extends AntDesignCommonInterface {
    range: boolean;
    min: number;
    max: number;
    step: number;
    vertical: boolean;
    marks: any;
    graduated: boolean;
    reversed: boolean;
}