import random from 'random';
import { generateLabel } from './formDataGeneratorUtils';

function generateRangeData() {
    return {
        label: generateLabel({ canBeEmpty: true }),
        value: random.uniformInt(-100, 100),
        min: -100,
        max: 100,
    }
}

export default generateRangeData;