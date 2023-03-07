import { Component } from 'react';
import Form from 'react-bootstrap/Form';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import { LibraryComponentGenerator } from '../../models/libraries/libraryComponentGenerator';
import { NumericInputParameterDistribution } from '../../models/distribution/inputs/numericInput';
import { NumericInputMapper } from '../../models/libraries/bootstrap/mappers/numericInputMapper';
import { LabelFloatingEnum } from '../../models/interfaces/primitives/label';
import { ValidationMapper } from '../../models/libraries/bootstrap/mappers/validationMapper';
import { ValidationStateEnum } from '../../models/interfaces/primitives/validation';


export default class NumericInput extends Component<any, any> {
    constructor(props) {
        super(props);
        this.state = {};
    }

    componentDidMount(): void {
        const {
            label,
            disabled,
            isValid,
            isInvalid,
            floating,
            readonly,
            value,
            min,
            max,
            step,
            validation
        } = LibraryComponentGenerator.generateComponent(
            new NumericInputParameterDistribution(),
            NumericInputMapper,
        );
    
        const {
            state: validationState,
            message: validationMessage,
        } = LibraryComponentGenerator.generateComponentFromSample(
            validation,
            ValidationMapper,
        );
        this.setState({
            label,
            disabled,
            isValid,
            isInvalid,
            floating,
            readonly,
            value,
            min,
            max,
            step,
            validationState,
            validationMessage,
        });
    }

    render() {
        const {
            label,
            disabled,
            isValid,
            isInvalid,
            floating,
            readonly,
            value,
            min,
            max,
            step,
            validationState,
            validationMessage,
        } = this.state;

        if (floating === LabelFloatingEnum.FLOATING && label !== '') {
            return (
                <Form.Group className="was-validated">
                    <FloatingLabel label={label}>
                        <Form.Control
                            type="number"
                            disabled={disabled}
                            isValid={isValid}
                            isInvalid={isInvalid}
                            readOnly={readonly}
                            defaultValue={value}
                            step={step}
                            min={min}
                            max={max}
                        />
                    </FloatingLabel>
                    {validationState !== ValidationStateEnum.UNKNOWN &&
                        <Form.Control.Feedback type={validationState}>
                            {validationMessage}
                        </Form.Control.Feedback>
                    }
                </Form.Group>
            );
        }
    
        return (
            <Form.Group className="was-validated">
                <Form.Label>{label}</Form.Label>
                <Form.Control
                    type="number"
                    disabled={disabled}
                    isValid={isValid}
                    isInvalid={isInvalid}
                    readOnly={readonly}
                    defaultValue={value}
                    step={step}
                    min={min}
                    max={max}
                />
                {validationState !== ValidationStateEnum.UNKNOWN &&
                    <Form.Control.Feedback type={validationState}>
                        {validationMessage}
                    </Form.Control.Feedback>
                }
            </Form.Group>
        );
    }
}