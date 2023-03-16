import { Form } from 'react-bootstrap';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { TextAreaInputParameterDistribution } from '../../models/distribution/inputs/textareaInput';
import { TextAreaMapper } from '../../models/libraries/bootstrap/mappers/textareaMapper';
import BootstrapInputItem from './BootstrapInputItem';

export default function BootstrapTextArea() {
    const props = LibraryComponentGenerator.generateComponent(
        new TextAreaInputParameterDistribution(),
        TextAreaMapper,
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
            }) => (
                <Form.Control
                    as="textarea"
                    disabled={disabled}
                    plaintext={plaintext}
                    readOnly={readonly}
                    defaultValue={defaultValue}
                    placeholder={placeholder}
                    isValid={isValid}
                    isInvalid={isInvalid}
                />
            )}
        </BootstrapInputItem>

    )
}