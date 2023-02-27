import _ from 'lodash';
import random from 'random';
import RandExp from 'randexp';
import {
    generateLabel,
    generateFeedback,
    generateBoolean,
    generateText,
} from './formDataGeneratorUtils';

function generateRandomColor() {
    const colorChars = [
        '0', '1', '2', '3', '4',
        '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F',
    ];
    const colorCode = `#${_.join(
        _.map(
            _.range(6), () => random.choice(colorChars)
        ),
        ''
    )}`;
    return colorCode;
}

function generateRandomDate() {
    const year = random.poisson(2023)();
    const month = 1 + random.choice(_.range(12));
    const day = 1 + random.choice(_.range(28));
    const date = `${year}-${month}-${day}`;
    return date;
}

function generateRandomTime() {
    const hour = 1 + random.choice(_.range(12));
    const minute = random.choice(_.range(60));
    const ampm = random.choice(['AM', 'PM']);
    const time = `${hour}:${minute} ${ampm}`;
    return time;
}

function generateRandomDatetimeLocal() {
    const date = generateRandomDate();
    const time = generateRandomTime();
    return `${date}, ${time}`;
}

function generateRandomEmail() {
    const username =  generateText({ exactly: 2, join: '' });
    const server =  generateText({ exactly: 1 });
    const email = `${username}@${server}.com`;
    return email;
}

function generateRandomMonth() {
    const months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]
    const year = random.poisson(2023)();
    const chosenMonth = random.choice(months);
    const month = `${chosenMonth} ${year}`;
    return month;
}

function generateRandomNumber() {
    const number = random.uniformInt(-100, 100);
    return number;
}

function generateRandomTel() {
    const regex = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;
    const tel = new RandExp(regex).gen();
    return tel;
}

function generateRandomText() {
    const text = generateText({ min: 1, max: 3, join: ' ' });
    return text;
}

function generateRandomUrl() {
    const protocol = random.choice(['http', 'https']);
    const websiteUrl =  generateText({ min: 1, max: 3, join: '.' });
    const url = `${protocol}://www.${websiteUrl}.com`;
    return url;
}

function generateRandomWeek() {
    const year = random.poisson(2023)();
    const weekNumber = random.uniformInt(1, 52);
    const weekPadded = _.pad(`${weekNumber}`, 2, '0');
    const week = `Week ${weekPadded}, ${year}`;
    return week;
}

function generateTextareaRows() {
    const rows = 1 + random.poisson(3);
    return rows;
}

function generateInputControl({ inputType }) {
    let inputControls = [
        'input',
        'textarea'
    ];
    if (inputType) {
        inputControls = [inputType];
    }
    const inputTypes = [
        'color',
        'date',
        'datetime-local',
        'email',
        'file',
        'month',
        'number',
        'password',
        'search',
        'tel',
        'text',
        'time',
        'url',
        'week',
    ];
    const inputTypeRandomDefaultValueGenerators = {
        color: generateRandomColor,
        date: generateRandomDate,
        'datetime-local': generateRandomDatetimeLocal,
        email: generateRandomEmail,
        month: generateRandomMonth,
        number: generateRandomNumber,
        password: generateRandomText,
        search: generateRandomText,
        tel: generateRandomTel,
        text: generateRandomText,
        time: generateRandomTime,
        url: generateRandomUrl,
        week: generateRandomWeek,
    }

    const control = random.choice(inputControls);

    const hasDefaultValue = generateBoolean();
    const hasPlaceholder = generateBoolean();

    const isReadonly = generateBoolean();
    const isValid = generateBoolean();
    const isDisabled = generateBoolean();

    const label = generateLabel({ canBeEmpty: false });
    const feedback = generateFeedback({ canBeEmpty: true });
    
    if (control === 'input') {
        const inputType = random.choice(inputTypes);
        let value = null;
        let placeholder = null;
        
        if (inputType !== 'file' && hasDefaultValue) {
            value = inputTypeRandomDefaultValueGenerators[inputType]();
        }
        if (inputType !== 'file' && hasPlaceholder) {
            placeholder = inputTypeRandomDefaultValueGenerators[inputType]();
        }

        return {
            control,
            type: inputType,
            value,
            placeholder,
            label,
            feedback,
            isReadonly,
            isValid,
            isDisabled,
        };
    }
    else {
        let value = hasDefaultValue ? generateRandomText() : null;
        let placeholder = hasDefaultValue ? generateRandomText() : null;

        const rows = generateTextareaRows();

        return {
            control,
            type: 'text',
            value,
            placeholder,
            label,
            feedback,
            rows,
            isReadonly,
            isValid,
            isDisabled,
        }
    }
}

export default generateInputControl;