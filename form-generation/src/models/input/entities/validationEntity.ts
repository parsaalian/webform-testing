export enum ValidationState {
    UNKNOWN = 1,
    VALID = 2,
    ERROR = 3,
    WARNING = 4,
}

export class Validation {
    constructor(
        private readonly state: ValidationState,
        private readonly message: string
    ) {
        this.state = state;
        this.message = message;
    }

    getState(): ValidationState {
        return this.state;
    }

    getMessage(): string {
        return this.message;
    }
}
