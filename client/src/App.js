import React from 'react';
import { Provider } from 'react-redux';
import './App.css';

import store from './store/store.configure'

import 'antd/dist/antd.css';
import {ConfigProvider} from 'antd';
import ruRu from 'antd/es/locale/ru_RU';

import Main from './components/main/main'

function App() {
  return (
      <Provider store={store}>
        <ConfigProvider locale={ruRu}>
          <Main />
        </ConfigProvider>
      </Provider>
  );
}

export default App;
