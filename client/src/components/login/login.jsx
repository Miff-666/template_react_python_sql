import React from "react";
import styles from './login.module.css'
import { Input, Button, Row, Col, Typography, Alert } from 'antd';


const Login = (props)=>{
    const style = { padding: '15px 0' };
    return(
        <div className={styles.parent}>
            <Row style={style} type="flex" align="middle">
                <Col span={6}>
                    <Typography.Text align="middle">
                        {props.store.global.input_token_text}
                    </Typography.Text>
                </Col>
                <Col span={18}>
                    <Input
                        placeholder={props.store.global.input_token_description}
                        name="username"
                        size={'large'}
                        width={'100%'}
                        value={props.store.global.input_token_value}
                        onChange={(e)=>{props.action.global.input_token_change(e.target.value)}}
                    />
                </Col>
            </Row>

            {props.store.global.error_auth_show?
                <Row style={style} type="flex" align="middle">
                    <Alert message={props.store.global.error_auth_text} type="error" />
                </Row>:
                null}

            <Row style={style} type="flex" align="middle">
                <Col span={24}>
                    <Button
                        type="primary"
                        size={'large'}
                        onClick={()=>props.action.global.auth(
                            props.store.global.input_token_value
                        )}
                        htmlType="submit"
                        style={{float: 'right'}}
                    >
                        {props.store.global.login_btn_text}
                    </Button>
                </Col>
            </Row>
        </div>
    )
}

export default Login