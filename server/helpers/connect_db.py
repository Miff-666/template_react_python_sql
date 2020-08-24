import asyncpg
import asyncio
import yaml
from helpers.config import Config


async def init_pg(app):
    config = Config.get_config()
    app['db'] = (await asyncpg.connect(**config['db']))


async def close_pg(app):
    await app['db'].close()
    del app['db']
