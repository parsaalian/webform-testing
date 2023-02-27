import {
    DiscreteValuedDistribution,
    WordDistribution,
    EntityDistribution
} from './distribution';

export class InputDistribution extends EntityDistribution {
    constructor() {
        const distributions = {
            label: new WordDistribution(
                {
                    min: 1,
                    max: 3,
                    join: ' ',
                },
                new DiscreteValuedDistribution([true, false], [0.2, 0.8]),
            ),
            disabled: new DiscreteValuedDistribution(
                [true, false],
                [0.2, 0.8]
            ),
            readonly: new DiscreteValuedDistribution(
                [true, false],
                [0.2, 0.8]
            ),
            required: new DiscreteValuedDistribution(
                [true, false],
                [0.2, 0.8]
            ),
            helper: new WordDistribution(
                {
                    min: 3,
                    max: 25,
                    join: ' ',
                },
                new DiscreteValuedDistribution([true, false], [0.8, 0.2]),
            ),
            placeholder: new WordDistribution(
                {
                    min: 1,
                    max: 3,
                    join: ' ',
                },
                new DiscreteValuedDistribution([true, false], [0.8, 0.2]),
            ),
        }
        super({
            parentDistribution: null,
            distributions,
        });
    }
}
