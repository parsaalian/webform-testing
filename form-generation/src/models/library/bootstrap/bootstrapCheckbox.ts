import { BinaryCheckboxEntity } from '../../input/entities/checkboxEntity';
import { CheckboxDistribution } from '../../distributions/data/checkboxDistribution';

export class BootstrapCheckbox extends BinaryCheckboxEntity {
    constructor() {
        const {
            label,
            disabled,
            readonly,
            required,
            helper,
            placeholder,
            defaultValue,
        } = new CheckboxDistribution().generateInstance();
        super({
            label,
            disabled,
            readonly,
            required,
            helper,
            placeholder,
            defaultValue,
        });
    }

    getValuesJson(): any {
        return {
            label: this.getLabel(),
            disabled: this.getDisabled(),
            readonly: this.getReadonly(),
            required: this.getRequired(),
            helper: this.getHelper(),
            placeholder: this.getPlaceholder(),
            defaultValue: this.getDefaultValue(),
        };
    }
}