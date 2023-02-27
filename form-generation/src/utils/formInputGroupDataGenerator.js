import _ from 'lodash';
import random from 'random';
import {
    generateLabel,
    generateFeedback,
    generateText
} from './formDataGeneratorUtils';
import generateInputControl from './formControlDataGenerator';

function allocateSegments() {
    const leftSideCount = random.poisson(1)();
    const middleCount = random.poisson(1)();
    const rightSideCount = random.poisson(1)();
    let segments = [];
    let leftSideHasSpecialComponent = false;
    let rightSideHasSpecialComponent = false;

    for (let i = 0; i < leftSideCount; i++) {
        let component;
        if (leftSideHasSpecialComponent) {
            component = random.choice(['button', 'text']);
        }
        else {
            component = random.choice(['text', 'checkbox', 'radio', 'button', 'dropdown']);
        }
        if (component !== 'text' && component !== 'button') {
            leftSideHasSpecialComponent = true;
        }
        segments.push(component);
    }
    for (let i = 0; i < middleCount; i++) {
        const component = random.choice(['input']);
        segments.push(component);
    }
    for (let i = 0; i < rightSideCount; i++) {
        let component;
        if (rightSideHasSpecialComponent) {
            component = random.choice(['button', 'text']);
        }
        else {
            component = random.choice(['text', 'checkbox', 'radio', 'button', 'dropdown']);
        }
        if (component !== 'text' && component !== 'button') {
            rightSideHasSpecialComponent = true;
        }
        segments.push(component);
    }

    return segments;
}

function generateInputGroupData() {
    const segments = allocateSegments();

    const data = segments.map((segment) => {
        if (segment === 'button') {
            return {
                type: 'button',
                label: generateText({ min: 1, max: 2, join: ' ' }),
            }
        }
        if (segment === 'text') {
            return {
                type: 'text',
                text: generateText({ min: 1, max: 2, join: ' ' }),
            }
        }
        if (segment === 'checkbox' || segment === 'radio') {
            return {
                type: segment,
                label: generateText({ min: 1, max: 2, join: ' ' }),
            }
        }
        if (segment === 'dropdown') {
            return {
                type: 'dropdown',
                label: generateText({ min: 1, max: 2, join: ' ' }),
                options: _.map(_.range(1 + random.poisson(2)()), () => 
                    generateText({ min: 1, max: 2, join: ' ' })
                ),
            }
        }
        return generateInputControl();
    });

    return {
        label: generateLabel({ canBeEmpty: true }),
        feedback: generateFeedback({ canBeEmpty: true }),
        data,
    };
}

export default generateInputGroupData;