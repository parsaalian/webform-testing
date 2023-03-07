import { InputNumber } from 'antd';
import { NumericInputParameterDistribution } from '../../models/interfaces/distribution/inputs/numericInput';
import { InputNumberMapper } from '../../models/libraries/antd/mappers/inputNumberMapper';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignInputNumber() {
    return (
        <AntDesignInputItem
            Distribution={NumericInputParameterDistribution}
            Mapper={InputNumberMapper}
            hasExternalLabel={true}
        >
            {({
                disabled,
                defaultValue,
                min,
                max,
                step,
            }) => (
                <InputNumber
                    disabled={disabled}
                    defaultValue={defaultValue}
                    min={min}
                    max={max}
                    step={step}
                />
            )}
        </AntDesignInputItem>
    );
}