import React from 'react';
import { Link } from "react-router-dom";

function Root() {
    return (
        <div>
            <Link to="/antd">Ant Design</Link>
            <br />
            <Link to="/bootstrap">Bootstrap</Link>
        </div>
    );
}

export default Root;