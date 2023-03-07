import _ from 'lodash';
import { AntDesignSelect } from "../interfaces/select";
import { ISelect, SelectOptions } from "../../../componentModels/inputs/select";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class SelectMapper extends AntDesignCommonMapper {
    public static mapValues(select: ISelect): AntDesignSelect {
        const {
            options,
            tagLimits,
            selected,
            mode,
        } = select;
        
        const mappedMode = mode || 'default';
        const mappedSelected = this.generateDefaultSelectedOptions(options, selected, mode);

        return {
            ...this.mapCommonValues(select),
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