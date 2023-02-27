import {
    generateLabel,
    generateFeedback,
    generateBoolean
} from './formDataGeneratorUtils';

function generateFormCheckData({
    labelCanBeEmpty,
    feedbackCanBeEmpty,
}) {
    return {
        label: generateLabel({ canBeEmpty: labelCanBeEmpty }),
        feedback: generateFeedback({ canBeEmpty: feedbackCanBeEmpty }),
        isValid: generateBoolean(),
    };
}

export default generateFormCheckData;