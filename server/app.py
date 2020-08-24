from aiohttp import web
import asyncio
import json
from handlers.auth import Auth
from handlers.save_settings import SaveSettings
# from handlers.ns import NS
from helpers.config import Config
from logging import config as logger_config
from helpers.connect_db import init_pg, close_pg
# from handlers.check_health import CheckHealth
# from helpers.metrics import (MetricsFactory, MetricsConst)
#
config = Config.get_config()
logger_config.dictConfig(config.get('logging'))


async def frontend(request):
    if request.content_length != 0:
        result = None
        try:
            db = request.app['db']
            jsn = await request.json()
            if jsn['type'] == 'auth':  # запрос авторизации
                auth = Auth(jsn, db)
                return await auth.check()
            elif jsn['type'] == 'save':
                save_settings = SaveSettings(jsn, db)
                return await save_settings.save()
        except Exception as e:
            # await (MetricsFactory(db)).inc(MetricsConst.Frontend.error)
            return web.json_response(str(e), status=400)
    else:  # пустой запрос
        # await (MetricsFactory(db)).inc(MetricsConst.Frontend.error)
        return web.json_response(
            {"error": {"message": "Empty request"}},
            status=204
        )


# async def api(request):
#     if request.content_length != 0:
#         result = None
#         try:
#             db = request.app['db']
#             jsn = await request.json()
#             if "TEST" in jsn:  # запрос авторизации
#                pass
#         except Exception as e:
#             # await (MetricsFactory(db)).inc(MetricsConst.Frontend.error)
#             return web.json_response(str(e), status=400)
#     else:  # пустой запрос
#         # await (MetricsFactory(db)).inc(MetricsConst.Frontend.error)
#         return web.json_response(
#             {"error": {"message": "Empty request"}},
#             status=204
#         )


# async def ns(request):
#     if request.content_length != 0:
#         result = None
#         try:
#             db = request.app['db']
#             jsn = await request.json()
#             if "TEST" in jsn:  # запрос авторизации
#                pass
#         except Exception as e:
#             # await (MetricsFactory(db)).inc(MetricsConst.Frontend.error)
#             return web.json_response(str(e), status=400)
#     else:  # пустой запрос
#         # await (MetricsFactory(db)).inc(MetricsConst.Frontend.error)
#         return web.json_response(
#             {"error": {"message": "Empty request"}},
#             status=204
#         )


app = web.Application()
app.router.add_route('POST', '/{project_name}/api/', frontend)  # запрос от фронта
# app.router.add_route('POST', '/{project_name}/api/{id}/', api)  # запрос от внешнего сервера crm
# app.router.add_route('POST', '/{project_name}/api/{action}/', ns)  # прием от нашего нс уведомления
# app.router.add_route('GET', '/{project_name}/api/health/', (CheckHealth).get)
#
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
#
web.run_app(app, **config['server'])
