import { Form } from "react-bootstrap";
import { LibraryComponentGenerator } from "../../models/libraries/libraryComponentGenerator";
import { BooleanInputParameterDistribution } from "../../models/distribution/inputs/booleanInput";
import { CheckMapper } from "../../models/libraries/bootstrap/mappers/checkMapper";
import BootstrapInputItem from "./BootstrapInputItem";

function BootstrapCheck({ type }) {
    const props = LibraryComponentGenerator.generateComponent(
        new BooleanInputParameterDistribution(),
        CheckMapper,
    );

    const {
        label,
        isValid,
        isInvalid,
        validationState,
        validationMessage,
    } = props;

    return (
        <BootstrapInputItem {...props} hasExternalLabel={false} hasExternalFeedback={false}>
            {({
                disabled,
                defaultValue,
            }) => (
                <Form.Check
                    id={label}
                    type={type}
                    label={label}
                    disabled={disabled}
                    defaultChecked={defaultValue}
                    isValid={isValid}
                    isInvalid={isInvalid}
                    feedback={validationState !== '' ? validationMessage : null}
                />
            )}
        </BootstrapInputItem>
    )
}

export function BootstrapCheckbox(props) {
    return <BootstrapCheck type="checkbox" {...props} />
}

export function BootstrapRadio(props) {
    return <BootstrapCheck type="radio" {...props} />
}

export function BootstrapSwitch(props) {
    return <BootstrapCheck type="switch" {...props} />
}