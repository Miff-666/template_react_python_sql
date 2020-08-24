import * as axios from "axios";

const instance = axios.create({
    baseURL: 'http://127.0.0.1:10000/template/api/',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
});

const sendAPI = {
    login,
    save,
}

function login(token) {
    return instance.post(`/`, {'type': 'auth', "token": token});
}

function save(app_id, is_integration){
    return instance.post(`/`,
        {
            'type': 'save',
            'is_integration': is_integration,
            'app_id': app_id
        });
}
export default sendAPI