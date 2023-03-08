import { Slider } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignSlider(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={true}>
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