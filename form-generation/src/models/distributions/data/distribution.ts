import _ from 'lodash';
import random from 'random';
import randomWords from 'random-words';

interface IDistribution {
    generateValue(): any;
};

export class DiscreteValuedDistribution implements IDistribution {
    constructor(
        private readonly possibleValues: Array<any>,
        private readonly valueProbabilities: Array<number>,
    ) {}

    public generateValue(): any {
        const randomValue = random.uniform(0, 1)();
        let cumulativeProbability = 0;
        for (let i = 0; i < this.valueProbabilities.length; i++) {
            cumulativeProbability += this.valueProbabilities[i];
            if (randomValue <= cumulativeProbability) {
                return this.possibleValues[i];
            }
        }
        return this.possibleValues[this.possibleValues.length - 1];
    }
}

export class PoissonDistribution implements IDistribution {
    constructor(
        private readonly lambda: number,
    ) {}

    public generateValue(): number {
        return random.poisson(this.lambda)();
    }
}

export class WordDistribution implements IDistribution {
    constructor(
        private readonly randomWordsOptions: any,
        private readonly canBeEmptyDistribution: DiscreteValuedDistribution = new DiscreteValuedDistribution([true, false], [0.2, 0.8]),
    ) {}

    public generateValue(): string | string[] | null {
        if (this.canBeEmptyDistribution.generateValue()) {
            return null;
        }
        return randomWords(this.randomWordsOptions);
    }
}

export type ParameterListType = {
    [key: string]: IDistribution;
}

export class ParameterDistributionEntity {
    constructor(private readonly parameterList: ParameterListType) {}

    public setParameterDistribution(parameterName: string, distribution: IDistribution) {
        this.parameterList[parameterName] = distribution;
    }

    public generateValueForParameter(parameterName: string): any {
        const distribution = this.parameterList[parameterName];
        return distribution.generateValue();
    }
}

export abstract class EntityDistribution {
    private parentDistribution: EntityDistribution | null;
    private distributions: ParameterListType;
    private parameterDistributionEntity: ParameterDistributionEntity;

    constructor({
        parentDistribution,
        distributions = {},
    }) {
        this.parentDistribution = parentDistribution;
        this.distributions = distributions;
        this.parameterDistributionEntity = new ParameterDistributionEntity(this.distributions);
    }

    public setParameterDistribution(parameterName: string, distribution: any) {
        this.parameterDistributionEntity.setParameterDistribution(parameterName, distribution);
    }

    public generateInstance(): any {
        let instance = {};
        if (this.parentDistribution) {
            instance = this.parentDistribution.generateInstance();
        }
        for (const parameterName in this.distributions) {
            instance[parameterName] = this.parameterDistributionEntity.generateValueForParameter(parameterName);
        }
        return instance;
    }
}