import json
from aiohttp import web


class SaveSettings:
    _db = None
    _is_integration = None
    _app_id = None

    def __init__(self, jsn, db):
        self._db = db
        self._is_integration = jsn['is_integration']
        self._app_id = jsn['app_id']

    async def save(self):
        result_db = json.loads(
            (
                await self._db.fetchrow(
                    "SELECT update_setting($1,$2)",
                    bool(self._is_integration),
                    int(self._app_id)
                )
            )[0]
        )
        is_ok = False
        if 'success' in result_db:
            is_ok = result_db['success']
        return web.json_response(
                {'saved': is_ok},
                status=200
            )
