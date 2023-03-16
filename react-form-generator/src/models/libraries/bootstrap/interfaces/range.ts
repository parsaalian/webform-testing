import { BootstrapCommonInterface } from "../commonInterface";

export interface BootstrapRange extends BootstrapCommonInterface {
    min: number;
    max: number;
    step: number;
}