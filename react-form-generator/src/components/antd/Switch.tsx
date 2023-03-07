import { Switch } from "antd";
import { BooleanInputParameterDistribution } from "../../models/distribution/inputs/booleanInput";
import { SwitchMapper } from "../../models/libraries/antd/mappers/switchMapper";
import AntDesignInputItem from "./AntDesignInputItem";

export default function AntDesignSwitch() {
    return (
        <AntDesignInputItem
            Distribution={BooleanInputParameterDistribution}
            Mapper={SwitchMapper}
            hasExternalLabel={true}
        >
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