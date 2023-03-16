import { BootstrapNumericInput } from "../interfaces/numeric";
import { INumericInput } from "../../../componentModels/inputs/numericInput";
import { LabelFloatingEnum } from "../../../componentModels/primitives/label";
import { BootstrapCommonMapper } from "../commonMapper";

export class NumericMapper extends BootstrapCommonMapper {
    public static mapValues(numericInput: INumericInput): BootstrapNumericInput {
        const {
            label,
            readonly,
            min,
            max,
            step,
        } = numericInput;

        const mappedFloating = label ? label.floating === LabelFloatingEnum.FLOATING : false;
        const mappedPlaintext = readonly;
        const mappedReadOnly = readonly;
        const mappedStep = step || 1;
        const mappedMin = min || 0;
        const mappedMax = max || 100;

        return {
            ...this.mapCommonValues(numericInput),
            floating: mappedFloating,
            plaintext: mappedPlaintext,
            readonly: mappedReadOnly,
            step: mappedStep,
            min: mappedMin,
            max: mappedMax,
        };
    }
}