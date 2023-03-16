import { Form } from "react-bootstrap";
import { LibraryComponentGenerator } from "../../models/libraries/libraryComponentGenerator";
import { SliderParameterDistribution } from "../../models/distribution/inputs/slider";
import { RangeMapper } from "../../models/libraries/bootstrap/mappers/rangeMapper";
import BootstrapInputItem from "./BootstrapInputItem";

export default function BootstrapRange() {
    const props = LibraryComponentGenerator.generateComponent(
        new SliderParameterDistribution(),
        RangeMapper,
    );

    return (
        <BootstrapInputItem {...props} hasExternalLabel={true} hasExternalFeedback={true}>
            {({
                disabled,
                min,
                max,
                step,
                defaultValue,
            }) => (
                <Form.Range
                    disabled={disabled}
                    min={min}
                    max={max}
                    step={step}
                    defaultValue={defaultValue}
                />
            )}
        </BootstrapInputItem>
    )
}