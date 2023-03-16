import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { InputTypesEnum } from '../../models/distribution/grid/inputTypes';

import { GridParameterDistribution } from '../../models/distribution/grid/grid';
import { TextualInputParameterDistribution } from '../../models/distribution/inputs/textualInput';
import { BooleanInputParameterDistribution } from '../../models/distribution/inputs/booleanInput';
import { NumericInputParameterDistribution } from '../../models/distribution/inputs/numericInput';
import { SelectParameterDistribution } from '../../models/distribution/inputs/select';
import { SliderParameterDistribution } from '../../models/distribution/inputs/slider';

import { CheckMapper } from '../../models/libraries/bootstrap/mappers/checkMapper';
import { GeneralTextMapper } from '../../models/libraries/bootstrap/mappers/generalTextMapper';
import { NumericMapper } from '../../models/libraries/bootstrap/mappers/numericMapper';
import { RangeMapper } from '../../models/libraries/bootstrap/mappers/rangeMapper';
import { SelectMapper } from '../../models/libraries/bootstrap/mappers/selectMapper';
import { TextAreaMapper } from '../../models/libraries/bootstrap/mappers/textareaMapper';


const distributions = {
    [InputTypesEnum.CHECKBOX]: BooleanInputParameterDistribution,
    [InputTypesEnum.NUMBER]: NumericInputParameterDistribution,
    [InputTypesEnum.RADIO]: BooleanInputParameterDistribution,
    [InputTypesEnum.SELECT]: SelectParameterDistribution,
    [InputTypesEnum.SLIDER]: SliderParameterDistribution,
    [InputTypesEnum.SWITCH]: BooleanInputParameterDistribution,
    [InputTypesEnum.TEXT]: TextualInputParameterDistribution,
    [InputTypesEnum.TEXTAREA]: TextualInputParameterDistribution,
}

const mappers = {
    [InputTypesEnum.CHECKBOX]: CheckMapper,
    [InputTypesEnum.NUMBER]: NumericMapper,
    [InputTypesEnum.RADIO]: CheckMapper,
    [InputTypesEnum.SELECT]: SelectMapper,
    [InputTypesEnum.SLIDER]: RangeMapper,
    [InputTypesEnum.SWITCH]: CheckMapper,
    [InputTypesEnum.TEXT]: GeneralTextMapper,
    [InputTypesEnum.TEXTAREA]: TextAreaMapper,
}


function generateComponentProps(componentName) {
    if (distributions[componentName] && mappers[componentName]) {
        return LibraryComponentGenerator.generateComponent(
            new distributions[componentName](),
            mappers[componentName],
        );
    } else {
        return LibraryComponentGenerator.generateComponent(
            new TextualInputParameterDistribution(),
            GeneralTextMapper,
        );
    }
}

export function generateGrid() {
    const grid = new GridParameterDistribution(12).generateSample();

    return grid.rows.map((row) => ({
        columns: row.columns.map((column) => ({
            span: column.span,
            type: column.content,
            props: generateComponentProps(column.content),
        })),
    }));
}