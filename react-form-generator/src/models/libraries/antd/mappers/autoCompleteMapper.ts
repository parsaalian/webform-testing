import _ from 'lodash';
import { AntDesignAutoComplete } from '../interfaces/autoComplete';
import { ISelect } from "../../../componentModels/inputs/select";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class AutoCompleteMapper extends AntDesignCommonMapper {
    public static mapValues(select: ISelect): AntDesignAutoComplete {
        const {
            options,
            selected,
        } = select;

        const mappedSelected = selected.length > 0 ? options[selected[0]] : null;

        return {
            ...this.mapCommonValues(select),
            defaultValue: mappedSelected,
            options,
        }
    }
}