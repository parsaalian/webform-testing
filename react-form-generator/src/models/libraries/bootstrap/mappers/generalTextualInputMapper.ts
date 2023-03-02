import RandExp from "randexp";
import { BootstrapGeneralTextualInput } from "../interfaces/generalTextualInput";
import { IGeneralTextualInput } from "../../../interfaces/inputs/generalTextualInput";
import { ValidationStateEnum } from "../../../interfaces/primitives/validation";
import { LabelFloatingEnum } from "../../../interfaces/primitives/label";
import { RegexPatternGenerator } from "../../../utils/regexPatternGenerator";

export class GeneralTextualMapper {
    public static mapValues(generalTextualInput: IGeneralTextualInput): BootstrapGeneralTextualInput {
        const {
            label,
            disabled,
            validation,
            readonly,
            type,
            hint,
        } = generalTextualInput;
        
        const mappedLabel = label && label.value ? label.value : '';
        const mappedFloating = label ? label.floating : LabelFloatingEnum.NOT_FLOATING;
        const mappedDisabled = disabled;
        const mappedIsInvalid = (validation && validation.state === ValidationStateEnum.INVALID) || false;
        const mappedIsValid = (validation && validation.state === ValidationStateEnum.VALID) || false;
        const mappedPlaintext = readonly;
        const mappedReadOnly = readonly;
        const mappedType = type;
        const mappedPlaceholder = hint || '';
        const mappedValue = new RandExp(RegexPatternGenerator.generateRegexFromType(mappedType)).gen();

        return {
            label: mappedLabel,
            floating: mappedFloating,
            disabled: mappedDisabled,
            isInvalid: mappedIsInvalid,
            isValid: mappedIsValid,
            plaintext: mappedPlaintext,
            readOnly: mappedReadOnly,
            type: mappedType,
            value: mappedValue,
            placeholder: mappedPlaceholder,
            validation,
        };
    }
}