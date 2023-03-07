import { Slider } from 'antd';
import { SliderParameterDistribution } from '../../models/interfaces/distribution/inputs/slider';
import { SliderMapper } from '../../models/libraries/antd/mappers/sliderMapper';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignSlider() {
    return (
        <AntDesignInputItem
            Distribution={SliderParameterDistribution}
            Mapper={SliderMapper}
            hasExternalLabel={true}
        >
            {({
                disabled,
                defaultValue,
                min,
                max,
                step,
                marks,
                reversed,
                vertical,
                range,
                graduated,
            }) => (
                <Slider
                    disabled={disabled}
                    defaultValue={defaultValue}
                    min={min}
                    max={max}
                    step={graduated ? null : step}
                    marks={marks}
                    reverse={reversed}
                    vertical={vertical}
                    range={range}
                />
            )}
        </AntDesignInputItem>
    );
}