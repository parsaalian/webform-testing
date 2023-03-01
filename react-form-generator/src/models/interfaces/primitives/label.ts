export enum LabelPlacementEnum {
    TOP = 'top',
    BOTTOM = 'bottom',
    LEFT = 'left',
    RIGHT = 'right',
}

export enum LabelFloatingEnum {
    FLOATING = 'floating',
    NOT_FLOATING = 'not-floating',
}

export interface ILabel {
    value: string;
    placement: LabelPlacementEnum;
    floating: LabelFloatingEnum;
}