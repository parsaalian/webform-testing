import { BootstrapRange } from "../interfaces/range";
import { ISlider } from "../../../componentModels/inputs/slider";
import { BootstrapCommonMapper } from "../commonMapper";

export class RangeMapper extends BootstrapCommonMapper {
    public static mapValues(rangeInput: ISlider): BootstrapRange {
        const {
            min,
            max,
            step,
        } = rangeInput;

        return {
            ...this.mapCommonValues(rangeInput),
            min,
            max,
            step,
        };
    }
}