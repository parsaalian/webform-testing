// TODO: randomize margins and paddings
import React from 'react';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import random from 'random';
import RandomizedFormGroup from './RandomizedFormGroup';

function RandomizedFormGrid() {
    const rowsCount = 1 + random.poisson(2)();
    let rows = [];
    for (let i = 0; i < rowsCount; i++) {
        const colsCount = 1 + random.poisson(1)();
        let cols = [];
        for (let j = 0; j < colsCount; j++) {
            const colSize = 1 + random.poisson(Math.floor(12 / colsCount) - 1);
            cols = [...cols, colSize];
        }
        let colsSum = cols.reduce((accumulator, current) => {
            return accumulator + current;
        }, 0);
        cols = cols.map((col) => Math.floor(col / colsSum));
        colsSum = cols.reduce((accumulator, current) => {
            return accumulator + current;
        }, 0);
        cols[cols.length - 1] += 12 - colsSum;
        rows = [...rows, cols];
    }

    return (
        <Form>
            {rows.map((cols) => (
                <Row className="mb-3">
                    {cols.map((col) => (
                        <Col xs={col}>
                            <RandomizedFormGroup />
                        </Col>
                    ))}
                </Row>
            ))}
        </Form>
    );
}

export default RandomizedFormGrid;