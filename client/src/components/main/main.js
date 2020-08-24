import React, {Component} from 'react'
import { connect } from 'react-redux'

import Login from '../login/login'
import Setting from '../setting/setting'

import {action as global_action} from '../../action/global.action'

class Main extends Component {
    render(){
        return(
                <>
                    {this.props.store.global.is_auth?
                        <Setting {...this.props}/>:
                        <Login {...this.props}/>
                    }
                </>
            )
    }
}

//прокидываем данные из стор в пропс
const mapStateToProps = store => {
    return {
        store: store
    }
}

//прокидываем диспатч из стор в пропс
const mapDispatchToProps = dispatch => {
    return {
        action: {
            global: {
                auth: (token)=> dispatch(global_action.auth(token)),
                input_token_change: (val)=> dispatch(global_action.input_token_change(val)),
                save: (app_id, is_integration)=> dispatch(global_action.save(app_id, is_integration)),
                set_integration_status: (val)=> dispatch(global_action.set_integration_status(val)),
            }
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Main)