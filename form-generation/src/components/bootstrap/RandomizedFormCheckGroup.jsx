import React from 'react'
import random from 'random';
import RandomizedFormCheck from './RandomizedFormCheck';

function RandomizedFormCheckGroup() {
    const inline = random.choice([false, true]);
    const count = 1 + random.poisson(2)();

    let group = [];
    for (let i = 0; i < count; i++) {
        group = [...group, i];
    }

    return (
        <>
            {group.map((i) => (
                <RandomizedFormCheck key={i} inline={inline} />
            ))}
        </>
    );
}

export default RandomizedFormCheckGroup;