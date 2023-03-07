import _ from 'lodash';
import { AntDesignCascader } from "../interfaces/cascader";
import { ISelect, SelectOptions } from '../../../componentModels/inputs/select';
import { AntDesignCommonMapper } from './antdCommonMapper';

export class CascaderMapper extends AntDesignCommonMapper {
    public static mapValues(select: ISelect): AntDesignCascader {
        const {
            options,
            tagLimits,
            selected,
            mode,
        } = select;

        const mappedMode = mode !== 'single';
        const mappedSelected = this.mapKeyValues(this.generateDefaultSelectedOptions(options, selected, mode));
        const mappedOptions = this.mapKeyValues(options);

        return {
            ...this.mapCommonValues(select),
            maxTagCount: tagLimits,
            defaultValue: mappedSelected,
            multiple: mappedMode,
            options: mappedOptions,
        }
    }

    private static generateDefaultSelectedOptions(options: SelectOptions, selected: Array<number>, mode: string): SelectOptions {
        // this happens if mode is single
        if (!mode) {
            return _.map(_.head(selected), (index: number) => options[index % optionsLength]);
        }
        const optionsLength = options.length;
        return _.map(_.uniq(selected.map(i => i % optionsLength)), (index: number) => options[index % optionsLength]);
    }

    private static mapKeyValues(options: SelectOptions): SelectOptions {
        return _.map(options, (option: any) => {
            return {
                value: option.key,
                label: option.value,
                children: this.mapKeyValues(option.children),
            }
        });
    }
}