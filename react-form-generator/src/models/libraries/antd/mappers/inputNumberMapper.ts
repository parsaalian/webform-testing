import { AntDesignInputNumber } from "../interfaces/inputNumber";
import { INumericInput } from "../../../interfaces/inputs/numericInput";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class InputNumberMapper extends AntDesignCommonMapper {
    public static mapValues(input: INumericInput): AntDesignInputNumber {
        const {
            min,
            max,
            step,
        } = input;

        const mappedMin = min || 0;
        const mappedMax = max || 100;
        const mappedStep = step || 1;

        return {
            ...this.mapCommonValues(input),
            min: mappedMin,
            max: mappedMax,
            step: mappedStep,
        }
    }
}