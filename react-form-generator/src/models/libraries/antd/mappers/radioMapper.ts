import { AntDesignRadio } from "../interfaces/radio";
import { IBooleanInput } from "../../../componentModels/inputs/booleanInput";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class RadioMapper extends AntDesignCommonMapper {
    public static mapValues(booleanInput: IBooleanInput): AntDesignRadio {
        const {
            renderAs,
        } = booleanInput;

        const mappedRenderAs = this.getRenderAs(renderAs);

        return {
            ...this.mapCommonValues(booleanInput),
            renderAs: mappedRenderAs,
        }
    }

    public static getRenderAs(renderAs: any): any {
        if (renderAs && renderAs.type === 'button') {
            return renderAs;
        }
        return null;
    }
}