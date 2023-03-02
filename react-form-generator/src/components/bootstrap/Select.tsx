import Form from 'react-bootstrap/Form';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { SelectParameterDistribution } from '../../models/interfaces/distribution/inputs/select';
import { SelectMapper } from '../../models/libraries/bootstrap/mappers/selectMapper';

export default function Select() {
    const {
        label,
        disabled,
        isValid,
        isInvalid,
        options,
    } = LibraryComponentGenerator.generateComponent(
        new SelectParameterDistribution(),
        SelectMapper,
    );

    return (
        <Form.Group className="was-validated">
            <Form.Label>{label}</Form.Label>
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
        </Form.Group>
    );
}