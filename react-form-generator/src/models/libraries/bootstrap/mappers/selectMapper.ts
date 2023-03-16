import { BootstrapSelect } from "../interfaces/select";
import { ISelect } from "../../../componentModels/inputs/select";
import { BootstrapCommonMapper } from "../commonMapper";

export class SelectMapper extends BootstrapCommonMapper {
    public static mapValues(selectInput: ISelect): BootstrapSelect {
        const {
            options,
        } = selectInput;

        const mappedOptions = options.map((option) => ({
            key: option.key,
            value: option.value,
            children: null,
        })) || [];

        return {
            ...this.mapCommonValues(selectInput),
            options: mappedOptions,
        };
    }
}