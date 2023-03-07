import { AntDesignSlider } from "../interfaces/slider";
import { ISlider } from "../../../interfaces/inputs/slider";
import { AntDesignCommonMapper } from "./antdCommonMapper";

export class SliderMapper extends AntDesignCommonMapper {
    public static mapValues(slider: ISlider): AntDesignSlider {
        const {
            min,
            max,
            step,
            marks,
            isInverted,
            orientation,
            isRange,
            useMarksOnly,
        } = slider;

        const mappedMin = min || -100;
        const mappedMax = max || 100;
        const mappedStep = step ? 1 + step : 1;
        const mappedMarks = this.mapMarks(marks, mappedMin, mappedMax);
        const mappedReverse = isInverted || false;
        const mappedVertical = orientation === "vertical";
        const mappedRange = isRange || false;
        const mappedGraduated = useMarksOnly || false;

        return {
            ...this.mapCommonValues(slider),
            min: mappedMin,
            max: mappedMax,
            step: mappedStep,
            marks: mappedMarks,
            reversed: mappedReverse,
            vertical: mappedVertical,
            range: mappedRange,
            graduated: mappedGraduated,
        }
    }

    public static mapMarks(marks: any, min: number, max: number): any {
        if (marks === true) {
            return {};
        }
        if (marks === false) {
            return null;
        }
        if (marks === null) {
            return null;
        }
        const mapper = (x: number) => min + x % (max - min);
        const mappedMarks: any = {};
        marks.forEach(mark => {
            mappedMarks[mapper(mark.key)] = mark.value;
        });
        return mappedMarks;
    }
}