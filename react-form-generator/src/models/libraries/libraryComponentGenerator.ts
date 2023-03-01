export class LibraryComponentGenerator {
    public static generateComponent(abstractComponent: any, targetLibraryMapper: any) {
        const instance = abstractComponent.generateSample();
        return targetLibraryMapper.mapValues(instance);
    }

    public static generateComponentFromSample(sampleComponent: any, targetLibraryMapper: any) {
        return targetLibraryMapper.mapValues(sampleComponent);
    }
}
