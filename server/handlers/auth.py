import json

from aiohttp import web
from helpers.dataapi import Dataapi


class Auth:
    _url_webhook = 'https://custom.uiscom.ru/livetex/api/webhook/'
    _jsn = None
    _app_id = None
    _dataapi = None
    _db = None
    _token = None
    _is_integration = False
    _timezone = None

    def __init__(self, jsn, db):
        self._jsn = jsn
        self._db = db
        if 'token' in self._jsn:
            self._token = self._jsn['token']
            self._dataapi = Dataapi(token=self._token)

    async def check(self):
        if self._dataapi is not None:
            result = {'is_auth': await self._check_auth()}
            if result['is_auth']:
                result['app_id'] = self._app_id
                result['is_integration'] = self._is_integration
                result['url_webhook'] = self._url_webhook + str(self._app_id)
            return web.json_response(
                result,
                status=200
            )
        else:
            return web.json_response(
                {'error': 'Нет токена'},
                status=400
            )

    async def _check_auth(self):
        res_jsn = await self._dataapi.get_account()
        if 'error' in res_jsn:
            return False
        else:
            self._app_id = res_jsn['result']['data'][0]['app_id']
            self._timezone = res_jsn['result']['data'][0]['timezone']
            # проверка интеграции в базе
            result_db = json.loads(
                (
                    await self._db.fetchrow(
                        "SELECT auth($1,$2,$3)",
                        str(self._token),
                        int(self._app_id),
                        str(self._timezone)
                    )
                )[0]
            )
            self._is_integration = result_db['is_integration']
            return True
