import { DiscreteValuedDistribution, EntityDistribution } from './distribution';
import { InputDistribution } from './inputDistribution';

export class CheckboxDistribution extends EntityDistribution {
    constructor() {
        const parentDistribution = new InputDistribution();
        const distributions = {
            defaultValue: new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
        };
        super({
            parentDistribution,
            distributions,
        });
    }
}