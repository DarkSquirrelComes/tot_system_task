from aiohttp import web

from db_engine import try_make_db
from routes import router


async def init_app() -> web.Application:
    await try_make_db()
    app = web.Application()
    app.add_routes(router)
    return app


web.run_app(init_app(), port=9000)
