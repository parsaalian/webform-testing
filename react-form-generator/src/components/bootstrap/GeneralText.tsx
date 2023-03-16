import { Form } from 'react-bootstrap';
import BootstrapInputItem from './BootstrapInputItem';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { GeneralTextualInputParameterDistribution } from '../../models/distribution/inputs/generalTextualInput';
import { GeneralTextMapper } from '../../models/libraries/bootstrap/mappers/generalTextMapper';


export default function BootstrapGeneralText() {
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
                type,
                isValid,
                isInvalid,
            }) => (
                <Form.Control
                    type={type}
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
    );
}