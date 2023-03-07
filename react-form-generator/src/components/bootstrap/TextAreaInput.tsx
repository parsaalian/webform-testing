import Form from 'react-bootstrap/Form';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { TextAreaInputParameterDistribution } from '../../models/distribution/inputs/textareaInput';
import { TextAreaInputMapper } from '../../models/libraries/bootstrap/mappers/textareaInputMapper';
import { LabelFloatingEnum } from '../../models/interfaces/primitives/label';
import { ValidationMapper } from '../../models/libraries/bootstrap/mappers/validationMapper';
import { ValidationStateEnum } from '../../models/interfaces/primitives/validation';

export default function TextAreaInput() {
    const {
        label,
        disabled,
        isValid,
        isInvalid,
        floating,
        readonly,
        value,
        validation,
        rows,
        placeholder,
    } = LibraryComponentGenerator.generateComponent(
        new TextAreaInputParameterDistribution(),
        TextAreaInputMapper,
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
                        as="textarea"
                        disabled={disabled}
                        isValid={isValid}
                        isInvalid={isInvalid}
                        readOnly={readonly}
                        defaultValue={value}
                        rows={rows}
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
                as="textarea"
                disabled={disabled}
                isValid={isValid}
                isInvalid={isInvalid}
                readOnly={readonly}
                defaultValue={value}
                rows={rows}
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