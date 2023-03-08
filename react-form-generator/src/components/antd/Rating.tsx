import { Rate } from 'antd';
import AntDesignInputItem from './AntDesignInputItem';

export default function AntDesignRating(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={true}>
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