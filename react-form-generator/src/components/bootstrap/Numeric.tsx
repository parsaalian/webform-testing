import { Form } from 'react-bootstrap';
import { GeneralTextualInputParameterDistribution } from '../../models/distribution/inputs/generalTextualInput';
import { GeneralTextMapper } from '../../models/libraries/bootstrap/mappers/generalTextMapper';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import BootstrapInputItem from './BootstrapInputItem';

export default function BootstrapNumeric() {
    const props = LibraryComponentGenerator.generateComponent(
        new GeneralTextualInputParameterDistribution(),
        GeneralTextMapper,
    );

    return (
        <BootstrapInputItem {...props} hasExternalLabel={true} hasExternalFeedback={true}>
            {({
                disabled,
                plaintext,
                readonly,
                defaultValue,
                placeholder,
                isValid,
                isInvalid,
                min,
                max,
                step,
            }) => (
                <Form.Control
                    type="number"
                    disabled={disabled}
                    plaintext={plaintext}
                    readOnly={readonly}
                    defaultValue={defaultValue}
                    placeholder={placeholder}
                    isValid={isValid}
                    isInvalid={isInvalid}
                    min={min}
                    max={max}
                    step={step}
                />
            )}
        </BootstrapInputItem>
    );
}