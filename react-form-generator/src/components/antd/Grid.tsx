import { Form, Row, Col } from 'antd';
import { generateGrid } from './formPropsGenerator';
import ErrorBoundary from '../error';
import AntDesignAutoComplete from './AutoComplete';
import AntDesignCascader from './Cascader';
import AntDesignCheckbox from './Checkbox';
import AntDesignDatePicker from './DatePicker';
import AntDesignInputNumber from './InputNumber';
import AntDesignRadio from './Radio';
import AntDesignSelect from './Select';
import AntDesignSlider from './Slider';
import AntDesignSwitch from './Switch';


function getChildComponent(childName, props) {
    switch (childName) {
        case "autoComplete":
            return <AntDesignAutoComplete {...props} />;
        case "cascader":
            return <AntDesignCascader {...props} />;
        case "checkbox":
            return <AntDesignCheckbox {...props} />;
        case "date":
            return <AntDesignDatePicker {...props} />;
        case "number":
            return <AntDesignInputNumber {...props} />;
        case "radio":
            return <AntDesignRadio {...props} />;
        case "select":
            return <AntDesignSelect {...props} />;
        case "slider":
            return <AntDesignSlider {...props} />;
        case "switch":
            return <AntDesignSwitch {...props} />;
        default:
            return <></>;
    }
}

function simplifyGenerationProperties(rows) {
    let inputs: any[] = [];

    console.log(rows);

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

    console.log(inputs);

    return JSON.stringify(inputs);
}

export default function AntDesignGrid() {
    const rows = generateGrid();

    return (
        <>
            <Form id="form">
                {rows.map((row, rowIndex) => (
                    <Row key={rowIndex}>
                        {row.columns.map((col, colIndex) => (
                            <Col key={colIndex} span={col.span}>
                                <ErrorBoundary>
                                    {getChildComponent(col.type, col.props)}
                                </ErrorBoundary>
                            </Col>
                        ))}
                    </Row>
                ))}
            </Form>
            <div id="json-object">
                {simplifyGenerationProperties(rows)}
            </div>
        </>
    );
}