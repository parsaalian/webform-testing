import _ from 'lodash';
import { AntDesignSelect } from "../interfaces/select";
import { ISelect, SelectOptions } from "../../../interfaces/inputs/select";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class SelectMapper extends AntDesignCommonMapper {
    public static mapValues(select: ISelect): AntDesignSelect {
        const {
            label,
            disabled,
            required,
            validation,
            options,
            tagLimits,
            selected,
            mode,
        } = select;
        
        const mappedLabel = label && label.value ? label.value : '';
        const mappedDisabled = disabled || false;
        const mappedRequired = required || false;
        const mappedMode = mode || 'default';
        const mappedSelected = this.generateDefaultSelectedOptions(options, selected, mode);
        const {
            validationState,
            validationMessage,
        } = this.mapValidation(validation);

        return {
            label: mappedLabel,
            disabled: mappedDisabled,
            required: mappedRequired,
            validationState,
            validationMessage,
            maxTagCount: tagLimits,
            defaultValue: mappedSelected,
            mode: mappedMode,
            options,
        }
    }

    private static generateDefaultSelectedOptions(options: SelectOptions, selected: Array<number>, mode: string): SelectOptions {
        if (mode === 'single') {
            return _.map(_.head(selected), (index: number) => options[index % optionsLength]);
        }
        const optionsLength = options.length;
        return _.map(_.uniq(selected.map(i => i % optionsLength)), (index: number) => options[index % optionsLength]);
    }
}