export enum LabelPlacementEnum {
    TOP = 'top',
    BOTTOM = 'bottom',
    LEFT = 'left',
    RIGHT = 'right',
}

export interface ILabel {
    value: string;
    placement: LabelPlacementEnum;
}