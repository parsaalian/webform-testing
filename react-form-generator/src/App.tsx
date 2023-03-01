import React from 'react';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import Root from './routes';
import Antd from './routes/antd';
import Bootstrap from './routes/bootstrap';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
  },
  {
    path: "/antd",
    element: <Antd />,
  },
  {
    path: '/bootstrap',
    element: <Bootstrap />,
  }
]);

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
