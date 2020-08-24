import { combineReducers } from 'redux';

import global_reducer from './global.reducer';


export const rootReducer = combineReducers({
    global: global_reducer,
})