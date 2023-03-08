import { Switch } from "antd";
import AntDesignInputItem from "./AntDesignInputItem";

export default function AntDesignSwitch(props) {
    return (
        <AntDesignInputItem {...props} hasExternalLabel={true}>
            {({
                disabled,
                defaultValue,
            }) => (
                <Switch
                    disabled={disabled}
                    defaultChecked={defaultValue}
                />
            )}
        </AntDesignInputItem>
    );
}