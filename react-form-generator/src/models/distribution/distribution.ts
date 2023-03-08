import _ from 'lodash';
import random from 'random';
import randomWords from 'random-words';
import RandExp from "randexp";
import { Nullify } from '../utils/modifiers';
import { ComponentParameterDistribution } from './componentParameterDistribution';

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
        return random.uniformInt(this.distributionParameters.min, this.distributionParameters.max)();
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

export class RegexDistribution extends AbstractDistribution<string> {
    constructor(
        regex: string,
    ) {
        super({ regex });
    }

    public generateSample(): string {
        return new RandExp(this.distributionParameters.regex).gen();
    }
}

export class RandomWordDistribution extends AbstractDistribution<Nullify<string | string[]>> {
    constructor(
        randomWordsOptions: any,
        canBeEmptyDistribution: DiscreteValuedDistribution<boolean> = new DiscreteValuedDistribution([true, false], [0.1, 0.9]),
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

export class RecursiveKeyValueDistribution extends AbstractDistribution<any> {
    constructor(subListCount: number, maxDepth: number, keyType: string = 'string') {
        super({
            subListCount,
            maxDepth,
            keyType,
        });
    }

    public generateSample(): any {
        return this.generateKeyValueList();
    }

    private generateKeyValueList(depth: number = 0): any {
        const count = 1 + random.poisson(this.distributionParameters.subListCount)();
        const list = _.map(_.range(count), () => ({
            key: this.distributionParameters.keyType === 'number' ? random.poisson(10000)() : randomWords({ exactly: 1, join: ' ' }),
            value: randomWords({ min: 1, max: 3, join: ' ' }),
            children: depth < this.distributionParameters.maxDepth ?
                random.choice([null, this.generateKeyValueList(depth + 1)]) :
                null,
        }));
        return list;
    }
}

export class ArrayOfDistribution extends AbstractDistribution<any> {
    constructor(
        countDistribution: IDistribution<number>,
        valueDistribution: IDistribution<any> | ComponentParameterDistribution
    ) {
        super({ countDistribution, valueDistribution });
    }

    public generateSample(): any {
        const count = this.distributionParameters.countDistribution.generateSample();
        return _.map(_.range(count), () => this.distributionParameters.valueDistribution.generateSample());
    }
}