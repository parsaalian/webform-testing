import 'antd/dist/reset.css';
import React from 'react';
import { Form, Input, Checkbox, Button, InputNumber, DatePicker } from 'antd';
import random from 'random';
import randomWords from 'random-words';

function generateFormAPIValues() {
    const colon = random.choice([false, true]);
    const disabled = random.choice([false, true]);
    const labelAlign = random.choice(['left', 'right']);
    const labelWrap = random.choice([false, true]);
    const layout = random.choice(['vertical', 'horizontal', 'inline']);
    const name = randomWords();
    const size = random.choice(['small', 'middle', 'large']);

    const wrapperColSpan = 1 + random.poisson(11)();
    // const wrapperColOffset = 1 + random.poisson(3)();
    const labelColSpan = Math.min(24 - wrapperColSpan, 1 + random.poisson(6)());
    // const labelColOffset = 1 + random.poisson(3)();

    return {
        colon,
        disabled,
        labelAlign,
        labelWrap,
        layout,
        name,
        size,
        labelCol: { span: labelColSpan, }, // offset: labelColOffset },
        wrapperCol: { span: wrapperColSpan, }, // offset: wrapperColOffset },
    };
}

function generateInputAPIValues() {
    const allowClear = random.choice([false, true]);
    const bordered = true; // random.choice([false, true]);
    const value = randomWords();
    const disabled = random.choice([false, true]);
    const showCount = random.choice([false, true]);
    const status = random.choice([null, 'warning', 'error']);
    const size = random.choice(['small', 'middle', 'large']);
    const type = random.choice(['text', 'password', 'email']);

    return {
        allowClear,
        bordered,
        value,
        disabled,
        showCount,
        status,
        size,
        type,
    };
}

function generateTextAreaAPIValues() {
    const allowClear = random.choice([false, true]);
    const autoSize = random.choice([false, true]);
    const bordered = true; // random.choice([false, true]);
    const value = randomWords();

    return {
        allowClear,
        autoSize,
        bordered,
        value,
    };
}

function generateNumberAPIValues() {
    const bordered = true; // random.choice([false, true]);
    const controls = random.choice([false, true]);
    const disabled = random.choice([false, true]);
    const readOnly = random.choice([false, true]);
    const status = random.choice([null, 'warning', 'error']);

    return {
        bordered,
        controls,
        disabled,
        readOnly,
        status,
    };
}

function generateCheckboxAPIValues() {
    const checked = random.choice([false, true]);
    const disabled = random.choice([false, true]);
    const indeterminate = random.choice([false, true]);

    return {
        checked,
        disabled,
        indeterminate,
    };
}

function generateDatePickerAPIValues() {
    const allowClear = random.choice([false, true]);
    const bordered = true;
    const disabled = random.choice([false, true]);
    const disabledDate = random.choice([false, true]);
    const inputReadOnly = random.choice([false, true]);
    const mode = random.choice(['time', 'date', 'month', 'year', 'decade']);
    const open = random.choice([false, true]);
    const picker = random.choice(['time', 'date', 'month', 'year', 'decade']);
    const placement = random.choice(['bottomLeft', 'bottomRight', 'topLeft', 'topRight']);
    const size = random.choice(['small', 'middle', 'large']);
    const status = random.choice([null, 'error', 'warning']);

    return {
        allowClear,
        bordered,
        disabled,
        disabledDate,
        inputReadOnly,
        mode,
        open,
        picker,
        placement,
        size,
        status,
    };
}

function generateInputList() {
    const count = 1 + random.poisson(1)();
    let inputList = [];
    for (let i = 0; i < count; i++) {
        const inputType = random.choice(['input', 'textarea', 'number', 'checkbox', 'datepicker']);
        let nextInput;
        if (inputType === 'input') {
            nextInput = [Input, randomWords(), generateInputAPIValues()];
        }
        else if (inputType === 'textarea') {
            nextInput = [Input.TextArea, randomWords(), generateTextAreaAPIValues()];
        }
        else if (inputType === 'number') {
            nextInput = [InputNumber, randomWords(), generateNumberAPIValues()];
        }
        else if (inputType === 'checkbox') {
            nextInput = [Checkbox, randomWords(), generateCheckboxAPIValues()];
        }
        else if (inputType === 'datepicker') {
            nextInput = [DatePicker, randomWords(), generateDatePickerAPIValues()];
        }
        inputList = [...inputList, nextInput];
    }
    return inputList;
}

function Antd() {
    const formAttributes = generateFormAPIValues();
    const inputList = generateInputList();

    return (
        <div>
            <Form {...formAttributes}>
                {inputList.map(([Component, name, attributes], i) => {
                    if (Component === Checkbox) {
                        return (
                            <Component key={i} {...attributes}>{name}</Component>
                        );
                    }
                    return (
                        <Form.Item
                            key={i}
                            label={name}
                            name={name}
                        >
                            <Component {...attributes} />
                        </Form.Item>
                    )
                })}

                <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
                    <Button type="primary" htmlType="submit">
                        Submit
                    </Button>
                </Form.Item>
            </Form>
        </div>
    );
}

export default Antd;