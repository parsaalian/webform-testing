import { Form, Row, Col } from 'react-bootstrap';
import { generateGrid } from './formPropsGenerator';
import ErrorBoundary from '../error';
import { InputTypesEnum } from '../../models/distribution/grid/inputTypes';
import BootstrapGeneralText from './GeneralText';
import BootstrapNumeric from './Numeric';
import BootstrapTextArea from './TextArea';
import BootstrapSelect from './Select';
import BootstrapRange from './Range';
import { BootstrapCheckbox } from './Check';
import { BootstrapRadio } from './Check';
import { BootstrapSwitch } from './Check';

const componentMap = {
    [InputTypesEnum.CHECKBOX]: BootstrapCheckbox,
    [InputTypesEnum.NUMBER]: BootstrapNumeric,
    [InputTypesEnum.RADIO]: BootstrapRadio,
    [InputTypesEnum.SELECT]: BootstrapSelect,
    [InputTypesEnum.SLIDER]: BootstrapRange,
    [InputTypesEnum.SWITCH]: BootstrapSwitch,
    [InputTypesEnum.TEXTAREA]: BootstrapTextArea,
    [InputTypesEnum.TEXT]: BootstrapGeneralText,
};

function getChildComponent(childName, props) {
    let Component;
    if (componentMap[childName]) {
        Component = componentMap[childName];
    }
    else {
        Component = BootstrapGeneralText;
    }

    return <Component {...props} />;
}

function simplifyGenerationProperties(rows) {
    let inputs: any[] = [];

    for (let row of rows) {
        for (let col of row.columns) {
            inputs.push({
                ...col.props,
                type: col.type,
                options: null,
                defaultValue: null,
            });
        }
    }

    return JSON.stringify(inputs);
}

export default function BootstrapGrid() {
    const rows = generateGrid();

    return (
        <>
            <div id="form">
                <Form>
                    {rows.map((row, rowIndex) => (
                        <Row key={rowIndex}>
                            {row.columns.map((col, colIndex) => (
                                <Col key={colIndex} xs={col.span}>
                                    <ErrorBoundary>
                                        {getChildComponent(col.type, col.props)}
                                    </ErrorBoundary>
                                </Col>
                            ))}
                        </Row>
                    ))}
                </Form>
            </div>
            <div id="json-object">
                {simplifyGenerationProperties(rows)}
            </div>
        </>
    );
}