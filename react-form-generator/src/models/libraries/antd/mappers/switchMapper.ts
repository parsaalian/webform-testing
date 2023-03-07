import { AntDesignSwitch } from "../interfaces/switch";
import { BooleanInputStateEnum, IBooleanInput } from "../../../componentModels/inputs/booleanInput";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class SwitchMapper extends AntDesignCommonMapper {
    public static mapValues(switchInput: IBooleanInput): AntDesignSwitch {
        const {
            value,
        } = switchInput;

        const mappedValue = value === BooleanInputStateEnum.CHECKED ? true : false;

        return {
            ...this.mapCommonValues(switchInput),
            defaultValue: mappedValue,
            text: null,
        };
    }
}