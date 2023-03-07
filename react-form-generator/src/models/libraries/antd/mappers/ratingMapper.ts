import { AntDesignRating } from "../interfaces/rating";
import { ISlider } from "../../../componentModels/inputs/slider";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class RatingMapper extends AntDesignCommonMapper {
    public static mapValues(slider: ISlider): AntDesignRating {
        const {
            max,
        } = slider;


        const mappedCount = max || 5;
        const mappedAllowHalf = true;

        return {
            ...this.mapCommonValues(slider),
            count: mappedCount,
            allowHalf: mappedAllowHalf,
        }
    }
}