import { Nullify } from "../../utils/modifiers";
import { IDistribution } from "./distribution";

export abstract class ComponentParameterDistribution {
    public parentDistribution: Nullify<ComponentParameterDistribution> = null;
    public parameters: { [key: string]: IDistribution<any> } = {};

    public generateSample(): { [key: string]: any } {
        let instance: { [key: string]: any } = {};
        if (this.parentDistribution) {
            instance = this.parentDistribution.generateSample();
        }
        for (let property in this.parameters) {
            instance[property] = this.parameters[property].generateSample();
        }
        return instance;
    }
}