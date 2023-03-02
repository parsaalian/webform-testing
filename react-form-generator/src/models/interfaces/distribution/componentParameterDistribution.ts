import _ from "lodash";
import { Nullify } from "../../utils/modifiers";
import { IDistribution } from "./distribution";

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
        if (_.isObject(propertyValue)) {
            return this.resolveSampleGeneration(_.mapValues(propertyValue, (value: any) => this.resolveSampleGeneration(value)));
        }
        if (_.isArray(propertyValue)) {
            return this.resolveSampleGeneration(_.map(propertyValue, (value: any) => this.resolveSampleGeneration(value)));
        }
        if (propertyValue instanceof ComponentParameterDistribution) {
            return this.resolveSampleGeneration(propertyValue.generateSample());
        }
        return propertyValue;
    }
}