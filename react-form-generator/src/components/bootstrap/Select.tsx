import Form from 'react-bootstrap/Form';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { SelectParameterDistribution } from '../../models/distribution/inputs/select';
import { SelectMapper } from '../../models/libraries/bootstrap/mappers/selectMapper';
import BootstrapInputItem from './BootstrapInputItem';

export default function BootstrapSelect() {
    const props = LibraryComponentGenerator.generateComponent(
        new SelectParameterDistribution(),
        SelectMapper,
    );
    const {
        isValid,
        isInvalid,
    } = props;

    return (
        <BootstrapInputItem {...props} hasExternalLabel={true} hasExternalFeedback={true}>
            {({
                disabled,
                options,
            }) => (
                <Form.Select
                disabled={disabled}
                isValid={isValid}
                isInvalid={isInvalid}

            >
                {options.map((option) => (
                    <option key={option.key} value={option.key}>
                        {option.value}
                    </option>
                ))}
            </Form.Select>
            )}
        </BootstrapInputItem>
    )
}