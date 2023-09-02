from typing import Callable

from app.urls import all_router
from core import server, FastAPI


def startup(app: FastAPI) -> Callable:
    async def app_start():
        # 挂接子路由
        all_router(app=app)
        # 异常拦截
        server.exception()
        # 链接数据库
        server.db_link()
        # 链接 redis 数据库
        app.state.check = server.redis_link(0)  # 验证码缓存
        app.state.cache = server.redis_link(1)  # 数据缓存
        print('启动完毕')

    return app_start


def stopping(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        print('停止')

    return stop_app
