import random from 'random';
import randomWords from 'random-words';
import { Nullify } from '../../utils/modifiers';

export type DistributionParametersType = {
    [key: string]: any;
};

export interface IDistribution<T> {
    distributionParameters: DistributionParametersType;
    generateSample(): T;
    getParameter(key: string): any;
    setParameter(key: string, value: any): void;
}

export abstract class AbstractDistribution<T> implements IDistribution<T> {
    public distributionParameters: DistributionParametersType;

    constructor(distributionParameters: DistributionParametersType) {
        this.distributionParameters = distributionParameters;
    }

    public getParameter(key: string): any {
        return this.distributionParameters[key];
    }

    public setParameter(key: string, value: any): void {
        this.distributionParameters[key] = value;
    }

    public abstract generateSample(): T;
}

export class DiscreteValuedDistribution<T> extends AbstractDistribution<T> {
    constructor(
        choices: Array<T>,
        probabilities: Array<number>,
    ) {
        super({ choices, probabilities });
    }

    public generateSample(): any {
        const {
            choices, probabilities,
        } = this.distributionParameters;
        const randomValue = random.uniform(0, 1)();
        let cumulativeProbability = 0;
        for (let i = 0; i < probabilities.length; i++) {
            cumulativeProbability += probabilities[i];
            if (randomValue <= cumulativeProbability) {
                return choices[i];
            }
        }
        return choices[choices.length - 1];
    }
}

export class ConstantValueDistribution extends AbstractDistribution<any> {
    constructor(
        value: any,
    ) {
        super({ value });
    }

    public generateSample(): any {
        return this.distributionParameters.value;
    }
}

export class UniformDistribution extends AbstractDistribution<number> {
    constructor(
        min: number,
        max: number,
    ) {
        super({ min, max });
    }

    public generateSample(): number {
        return random.uniform(this.distributionParameters.min, this.distributionParameters.max)();
    }
}

export class PoissonDistribution extends AbstractDistribution<number> {
    constructor(
        lambda: number,
    ) {
        super({ lambda });
    }

    public generateSample(): number {
        return random.poisson(this.distributionParameters.lambda)();
    }
}

export class RandomWordDistribution extends AbstractDistribution<Nullify<string | string[]>> {
    constructor(
        randomWordsOptions: any,
        canBeEmptyDistribution: DiscreteValuedDistribution<boolean> = new DiscreteValuedDistribution([true, false], [0.5, 0.5]),
    ) {
        super({ randomWordsOptions, canBeEmptyDistribution });
    }

    public generateSample(): Nullify<string | string[]> {
        if (this.distributionParameters.canBeEmptyDistribution.generateSample()) {
            return null;
        }
        return randomWords(this.distributionParameters.randomWordsOptions);
    }
}

export class NullDistribution extends AbstractDistribution<null> {
    constructor() {
        super({});
    }

    public generateSample(): null {
        return null;
    }
}