import _ from "lodash";
import { Nullify } from "../../utils/modifiers";
import { IDistribution, AbstractDistribution } from "./distribution";

export interface IComponentParameterDistribution {
    parentDistribution: Nullify<ComponentParameterDistribution>;
    parameters: { [key: string]: IDistribution<any> };
    generateSample(): { [key: string]: any };
}

export abstract class ComponentParameterDistribution {
    public parentDistribution: Nullify<ComponentParameterDistribution> = null;
    public parameters: { [key: string]: IDistribution<any> } = {};

    public generateSample(): { [key: string]: any } {
        let instance: { [key: string]: any } = {};
        if (this.parentDistribution) {
            instance = this.parentDistribution.generateSample();
        }
        for (let property in this.parameters) {
            instance[property] = this.resolveSampleGeneration(this.parameters[property]);
        }
        return instance;
    }

    private resolveSampleGeneration(propertyValue: any): any {
        if (this.isPlainObject(propertyValue)) {
            return propertyValue;
        }
        if (propertyValue instanceof AbstractDistribution || propertyValue instanceof ComponentParameterDistribution) {
            return this.resolveSampleGeneration(propertyValue.generateSample());
        }
        if (_.isArray(propertyValue)) {
            return this.resolveSampleGeneration(_.map(propertyValue, (value: any) => this.resolveSampleGeneration(value)));
        }
        if (_.isObject(propertyValue)) {
            return this.resolveSampleGeneration(_.mapValues(propertyValue, (value: any) => this.resolveSampleGeneration(value)));
        }
        return propertyValue;
    }

    private isPlainObject(value: any): boolean {
        if (typeof value === 'string' ||
            typeof value === 'number' ||
            typeof value === 'boolean' ||
            value === null ||
            value === undefined
        ) {
            return true;
        }
        if (value instanceof AbstractDistribution || value instanceof ComponentParameterDistribution) {
            return false;
        }
        return _.reduce(value, (result: boolean, value: any) => {
            return result && !(value instanceof AbstractDistribution) && !(value instanceof ComponentParameterDistribution)
        }, true);
    }
}