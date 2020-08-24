import { GLOBAL_CONST } from '../../action/global.action'

const initialState = {
    is_auth: false,
    input_token_text: 'Токен API',
    input_token_description: 'Введите токен API UIS',
    input_token_value: '',
    login_btn_text: 'Войти',
    error_auth_text: 'Неправильный токен или недостаточно прав у токена',
    error_auth_show: false,
    app_id: 0,
    is_integration: false,
    url_webhook: '',
}


export default function reducer(state = initialState, action) {
    switch (action.type) {
        case GLOBAL_CONST.SET_AUTH:
            return auth(state, action.payload)
        case GLOBAL_CONST.SET_TOKEN:
            return {...state, input_token_value: action.payload}
        case GLOBAL_CONST.SAVE:
            return {...state}
        case GLOBAL_CONST.SET_INTEGRATION_STATUS:
            return {...state, is_integration: action.payload}
        default:
            return state
    }
}

function auth(state, payload) {
    if(payload.is_auth){
        return {
            ...state,
            is_auth: payload.is_auth,
            app_id: payload.app_id,
            is_integration: payload.is_integration,
            url_webhook: payload.url_webhook,
            error_auth_show: false,
        }
    }else{
        return {
            ...state,
            is_auth: payload.is_auth,
            app_id: 0,
            error_auth_show: true,
        }
    }
}