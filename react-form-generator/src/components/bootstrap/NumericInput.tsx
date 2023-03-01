import Form from 'react-bootstrap/Form';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { NumericInputParameterDistribution } from '../../models/interfaces/distribution/inputs/numericInput';
import { NumericInputMapper } from '../../models/libraries/bootstrap/mappers/numericInputMapper';
import { LabelFloatingEnum } from '../../models/interfaces/primitives/label';

export default function NumericInput() {
    const {
        label,
        disabled,
        isValid,
        isInvalid,
        floating,
        // validation,
        readonly,
        value,
    } = LibraryComponentGenerator.generateComponent(
        new NumericInputParameterDistribution(),
        NumericInputMapper,
    );

    if (floating === LabelFloatingEnum.FLOATING && label !== '') {
        return (
            <Form.Group>
                <FloatingLabel label={label}>
                    <Form.Control
                        type="number"
                        disabled={disabled}
                        isValid={isValid}
                        isInvalid={isInvalid}
                        readOnly={readonly}
                        value={value}
                    />
                </FloatingLabel>
            </Form.Group>
        );
    }

    return (
        <Form.Group>
            <Form.Label>{label}</Form.Label>
            <Form.Control
                type="number"
                disabled={disabled}
                isValid={isValid}
                isInvalid={isInvalid}
                readOnly={readonly}
                defaultValue={value}
            />
        </Form.Group>
    );
}