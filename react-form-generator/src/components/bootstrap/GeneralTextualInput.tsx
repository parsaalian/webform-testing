import Form from 'react-bootstrap/Form';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { GeneralTextualInputParameterDistribution } from '../../models/distribution/inputs/generalTextualInput';
import { GeneralTextualMapper } from '../../models/libraries/bootstrap/mappers/generalTextualInputMapper';
import { LabelFloatingEnum } from '../../models/interfaces/primitives/label';
import { ValidationMapper } from '../../models/libraries/bootstrap/mappers/validationMapper';
import { ValidationStateEnum } from '../../models/interfaces/primitives/validation';

export default function GeneralTextualInput() {
    const {
        type,
        label,
        disabled,
        isValid,
        isInvalid,
        floating,
        readonly,
        value,
        validation,
        placeholder,
    } = LibraryComponentGenerator.generateComponent(
        new GeneralTextualInputParameterDistribution(),
        GeneralTextualMapper,
    );

    const {
        state: validationState,
        message: validationMessage,
    } = LibraryComponentGenerator.generateComponentFromSample(
        validation,
        ValidationMapper,
    );

    if (floating === LabelFloatingEnum.FLOATING && label !== '') {
        return (
            <Form.Group className="was-validated">
                <FloatingLabel
                    controlId="floatingInput"
                    label={label}
                    className={floating ? 'floating' : ''}
                >
                    <Form.Control
                        type="text"
                        disabled={disabled}
                        isValid={isValid}
                        isInvalid={isInvalid}
                        readOnly={readonly}
                        defaultValue={value}
                        placeholder={placeholder}
                    />
                    <Form.Control.Feedback type={validationState}>
                        {validationMessage}
                    </Form.Control.Feedback>
                </FloatingLabel>
            </Form.Group>
        );
    } 

    return (
        <Form.Group className="was-validated">
            <Form.Label>{label}</Form.Label>
            <Form.Control
                type={type}
                disabled={disabled}
                isValid={isValid}
                isInvalid={isInvalid}
                readOnly={readonly}
                defaultValue={value}
                placeholder={placeholder}
            />
            {validationState !== ValidationStateEnum.UNKNOWN &&
                <Form.Control.Feedback type={validationState}>
                    {validationMessage}
                </Form.Control.Feedback>
            }
        </Form.Group>
    );
}