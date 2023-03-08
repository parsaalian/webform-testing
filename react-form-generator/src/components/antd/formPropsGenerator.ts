import { GridParameterDistribution } from '../../models/distribution/grid/grid';
import { BooleanInputParameterDistribution } from '../../models/distribution/inputs/booleanInput';
import { DateTimeInputParameterDistribution } from '../../models/distribution/inputs/dateInput';
import { NumericInputParameterDistribution } from '../../models/distribution/inputs/numericInput';
import { SelectParameterDistribution } from '../../models/distribution/inputs/select';
import { SliderParameterDistribution } from '../../models/distribution/inputs/slider';
import { AutoCompleteMapper } from '../../models/libraries/antd/mappers/autoCompleteMapper';
import { CascaderMapper } from '../../models/libraries/antd/mappers/cascaderMapper';
import { CheckboxMapper } from '../../models/libraries/antd/mappers/checkboxMapper';
import { DatePickerMapper } from '../../models/libraries/antd/mappers/datePickerMapper';
import { InputNumberMapper } from '../../models/libraries/antd/mappers/inputNumberMapper';
import { RadioMapper } from '../../models/libraries/antd/mappers/radioMapper';
import { RatingMapper } from '../../models/libraries/antd/mappers/ratingMapper';
import { SelectMapper } from '../../models/libraries/antd/mappers/selectMapper';
import { SliderMapper } from '../../models/libraries/antd/mappers/sliderMapper';
import { SwitchMapper } from '../../models/libraries/antd/mappers/switchMapper';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';

function generateComponentProps(componentName) {
    switch (componentName) {
        case "autoComplete":
            return LibraryComponentGenerator.generateComponent(
                new SelectParameterDistribution(),
                AutoCompleteMapper,
            );
        case "cascader":
            return LibraryComponentGenerator.generateComponent(
                new SelectParameterDistribution(),
                CascaderMapper,
            );
        case "checkbox":
            return LibraryComponentGenerator.generateComponent(
                new BooleanInputParameterDistribution(),
                CheckboxMapper,
            );
        case "date":
            return LibraryComponentGenerator.generateComponent(
                new DateTimeInputParameterDistribution(),
                DatePickerMapper,
            );
        case "number":
            return LibraryComponentGenerator.generateComponent(
                new NumericInputParameterDistribution(),
                InputNumberMapper,
            );
        case "radio":
            return LibraryComponentGenerator.generateComponent(
                new BooleanInputParameterDistribution(),
                RadioMapper,
            );
        case "rate":
            return LibraryComponentGenerator.generateComponent(
                new SliderParameterDistribution(),
                RatingMapper,
            );
        case "select":
            return LibraryComponentGenerator.generateComponent(
                new SelectParameterDistribution(),
                SelectMapper,
            );
        case "slider":
            return LibraryComponentGenerator.generateComponent(
                new SliderParameterDistribution(),
                SliderMapper,
            );
        case "switch":
            return LibraryComponentGenerator.generateComponent(
                new BooleanInputParameterDistribution(),
                SwitchMapper,
            );
        default:
            return {};
    }
}

export function generateGrid() {
    const grid = new GridParameterDistribution(24).generateSample();

    return grid.rows.map((row) => ({
        columns: row.columns.map((column) => ({
            span: column.span,
            type: column.content,
            props: generateComponentProps(column.content),
        })),
    }));
}