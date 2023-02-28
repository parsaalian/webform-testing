import { NumericInputMapper } from "./models/libraries/bootstrap/mappers/numericInputMapper";
import { NumericInputParameterDistribution } from "./models/interfaces/distribution/inputs/numericInput";
import { LibraryComponentGenerator } from "./models/libraries/libraryComponentGenerator";

console.log(LibraryComponentGenerator.generateComponent(NumericInputParameterDistribution, NumericInputMapper));