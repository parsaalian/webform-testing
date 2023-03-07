import { Rate } from 'antd';
import { SliderParameterDistribution } from '../../models/distribution/inputs/slider';
import { RatingMapper } from '../../models/libraries/antd/mappers/ratingMapper';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignRating() {
    return (
        <AntDesignInputItem
            Distribution={SliderParameterDistribution}
            Mapper={RatingMapper}
            hasExternalLabel={true}
        >
            {({
                disabled,
                defaultValue,
                count
            }) => (
                <Rate
                    disabled={disabled}
                    count={count}
                    defaultValue={defaultValue}
                />
            )}
        </AntDesignInputItem>
    );
}