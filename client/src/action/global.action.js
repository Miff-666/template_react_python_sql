import Api from '../api/api'
import {message} from "antd";

export const GLOBAL_CONST = {
    SET_AUTH: 'SET_AUTH',
    SET_TOKEN: 'SET_TOKEN',
    SET_SELECT_USER_ID: 'SET_SELECT_USER_ID',
    SET_SELECT_SITE_ID: 'SET_SELECT_SITE_ID',
    SAVE: 'SAVE',
    SET_INTEGRATION_STATUS: 'SET_INTEGRATION_STATUS'
}

export const action = {
    auth,
    input_token_change,
    on_select_user,
    save,
    on_select_site,
    set_integration_status,
}

function auth(token){
    return dispatch => {
        let result = {
            is_auth: false,
        }
        Api.login(token)
            .then(
                (data)=>{
                    result = data.data;
                    console.log(result);
                    dispatch( {
                        type:GLOBAL_CONST.SET_AUTH,
                        payload: result
                    })
                }
            ).catch(
            (err)=>{
                console.log(result, err);
                dispatch(
                    {
                        type:GLOBAL_CONST.SET_AUTH,
                        payload: result
                    }
                )
            }
        )
    }
}

function input_token_change(val){
    return {
        type:GLOBAL_CONST.SET_TOKEN,
        payload: val,
    }
}

function on_select_user(val){
    return {
        type: GLOBAL_CONST.SET_SELECT_USER_ID,
        payload: val,
    }
}

function on_select_site(val){
    return {
        type: GLOBAL_CONST.SET_SELECT_SITE_ID,
        payload: val,
    }
}

function save(app_id, is_integration, select_user_id, select_site_id){
    return dispatch => {
        const key = 'сохранение';
        message.loading({ content: 'Сохранение...', key, duration: 0 });
        let result = {
            saved: false
        }
        Api.save(app_id, is_integration, select_user_id, select_site_id)
            .then(
                (response)=>{
                    switch (response.status){
                        case 200:
                            response.data.saved?
                                message.success({ content: 'Сохранено!', key, duration: 2 }):
                                message.error({ content: 'Не сохранено!', key, duration: 2 })
                            dispatch({
                                type: GLOBAL_CONST.SAVE,
                                payload: result.saved
                            } )
                            break
                        default:
                            message.error({ content: 'Не сохранено!', key, duration: 2 })
                            result = {
                                saved: false
                            }
                            dispatch({
                                type: GLOBAL_CONST.SAVE,
                                payload: result.saved
                            } )
                    }
                }
            ).catch(
            (err)=>{
                message.error({ content: 'Не сохранено!', key, duration: 2 })
                console.log(result, err);
                dispatch({
                    type: GLOBAL_CONST.SAVE,
                    payload: result.saved
                } )
            }
        )
    }
}

function set_integration_status(val) {
    return {
        type: GLOBAL_CONST.SET_INTEGRATION_STATUS,
        payload: val,
    }
}