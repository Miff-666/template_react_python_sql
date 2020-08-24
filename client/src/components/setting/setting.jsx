import React from "react";
import styles from './setting.module.css'
import {Input, Button, Row, Col, Typography, Alert, Select, message, Switch, Space} from 'antd';
import ExclamationCircleOutlined from "@ant-design/icons/lib/icons/ExclamationCircleOutlined";

const Setting = (props)=>{
    const style = { padding: '15px 0' };
    return(
        <div className={styles.parent}>
            <Row style={style} type="flex" align="middle">
                <Col span={10}>
                    <Typography.Text align="middle" style={{marginRight: '5px'}}>
                        Интеграция:
                    </Typography.Text>
                </Col>
                <Col span={14}>
                    <Switch
                        style={{float: 'right'}}  size={'large'}
                        checkedChildren="ВКЛ" unCheckedChildren="ВЫКЛ"
                        checked={props.store.global.is_integration}
                        onChange={(val)=>props.action.global.set_integration_status(val)}
                    />
                </Col>
            </Row>
            <Row style={style} type="flex" align="middle">
                <Col>
                    <Typography.Text align="middle" style={{marginRight: '5px'}} disabled={!props.store.global.is_integration}>
                        Адрес для вебхуков Livetex:
                    </Typography.Text>
                </Col>
                <Col>
                    <Typography.Text copyable={props.store.global.is_integration} code={true} disabled={!props.store.global.is_integration}>
                        {props.store.global.url_webhook}
                    </Typography.Text>
                </Col>
            </Row>
            <Row>
                <Col span={17}></Col>
                <Col span={7}>
                    <Button
                        type="primary"
                        size={'large'}
                        onClick={()=>props.action.global.save(
                            props.store.global.app_id,
                            props.store.global.is_integration,
                        )}
                        htmlType="submit"
                        style={{float: 'right'}}
                    >
                        Сохранить
                    </Button>
                </Col>
            </Row>
        </div>
    )
}

export default Setting