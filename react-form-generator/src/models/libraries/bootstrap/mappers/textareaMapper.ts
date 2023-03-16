import { BootstrapCommonMapper } from "../commonMapper";
import { BootstrapTextAreaInput } from "../interfaces/textarea";
import { ITextAreaInput } from "../../../componentModels/inputs/textareaInput";
import { LabelFloatingEnum } from "../../../componentModels/primitives/label";


export class TextAreaMapper extends BootstrapCommonMapper {
    public static mapValues(textAreaInput: ITextAreaInput): BootstrapTextAreaInput {
        const {
            label,
            readonly,
            rows,
            hint,
        } = textAreaInput;

        const mappedFloating = label ? label.floating === LabelFloatingEnum.FLOATING : false;
        const mappedPlaintext = readonly;
        const mappedReadOnly = readonly;
        const mappedRows = rows || 1;
        const mappedPlaceholder = hint || '';

        return {
            ...this.mapCommonValues(textAreaInput),
            floating: mappedFloating,
            plaintext: mappedPlaintext,
            readonly: mappedReadOnly,
            rows: mappedRows,
            placeholder: mappedPlaceholder,
        };
    }
}