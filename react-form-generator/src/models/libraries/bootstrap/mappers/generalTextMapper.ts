import { BootstrapCommonMapper } from "../commonMapper";
import { BootstrapGeneralTextualInput } from "../interfaces/generalText";
import { IGeneralTextualInput } from "../../../componentModels/inputs/generalTextualInput";
import { LabelFloatingEnum } from "../../../componentModels/primitives/label";

export class GeneralTextMapper extends BootstrapCommonMapper {
    public static mapValues(generalTextualInput: IGeneralTextualInput): BootstrapGeneralTextualInput {
        const {
            label,
            readonly,
            type,
            hint,
        } = generalTextualInput;

        const mappedFloating = label ? label.floating === LabelFloatingEnum.FLOATING : false;
        const mappedPlaintext = readonly;
        const mappedReadOnly = readonly;
        const mappedType = type;
        const mappedPlaceholder = hint || '';

        return {
            ...this.mapCommonValues(generalTextualInput),
            floating: mappedFloating,
            plaintext: mappedPlaintext,
            readonly: mappedReadOnly,
            type: mappedType,
            placeholder: mappedPlaceholder,
        };
    }
}