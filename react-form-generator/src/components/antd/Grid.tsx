import { Form, Row, Col } from 'antd';
import { GridParameterDistribution } from '../../models/distribution/grid/grid';
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

function getChildComponent(childName) {
    switch (childName) {
        case "autoComplete":
            return <AntDesignAutoComplete />;
        case "cascader":
            return <AntDesignCascader />;
        case "checkbox":
            return <AntDesignCheckbox />;
        case "date":
            return <AntDesignDatePicker />;
        case "number":
            return <AntDesignInputNumber />;
        case "radio":
            return <AntDesignRadio />;
        case "select":
            return <AntDesignSelect />;
        case "slider":
            return <AntDesignSlider />;
        case "switch":
            return <AntDesignSwitch />;
        default:
            return <></>;
    }
}

export default function AntDesignGrid() {
    const grid = new GridParameterDistribution(24).generateSample();

    return (
        <Form>
            {grid.rows.map((row, rowIndex) => (
                <Row key={rowIndex}>
                    {row.columns.map((col, colIndex) => (
                        <Col key={colIndex} span={col.span}>
                            <ErrorBoundary>
                                {getChildComponent(col.content)}
                            </ErrorBoundary>
                        </Col>
                    ))}
                </Row>
            ))}
        </Form>
    );
}