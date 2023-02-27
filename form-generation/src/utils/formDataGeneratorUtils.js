import random from 'random';
import randomWords from 'random-words';

export function generateBoolean() {
    const isValid = random.choice([false, true]);
    return isValid;
}

export function generateText({
    canBeEmpty,
    exactly,
    min,
    max,
    join,
}) {
    const generatedText = randomWords({ exactly, min, max, join });
    if (canBeEmpty) {
        return random.choice(['', generatedText]);
    }
    return generatedText;
}

export function generateLabel({
    canBeEmpty
}) {
    return generateText({ canBeEmpty, min: 1, max: 5, join: ' ' })
}

export function generateFeedback({
    canBeEmpty
}) {
    return generateText({ canBeEmpty, min: 3, max: 10, join: ' ' });
}