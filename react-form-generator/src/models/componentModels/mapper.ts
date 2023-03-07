export type KeysToNewType<Keys, NewType> = {
    [Property in keyof Keys]?: NewType
};