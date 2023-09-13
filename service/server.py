from typing import Union

import redis
from fastapi import FastAPI
from passlib.context import CryptContext
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from service import FastAPIException
from settings import setting


class Server:

    def __init__(self):
        self.app: Union[FastAPI, None] = None
        self.redis = None
        self.context = None

    def create_app(self) -> FastAPI:
        self.app = FastAPI(
            title=setting.TITLE,
            summary=setting.SUMMARY)

        return self.app

    def db_link(self):
        register_tortoise(
            self.app,
            config=setting.db_config,
            generate_schemas=True,
            add_exception_handlers=False, )

    def exception(self):
        FastAPIException(self.app)

    def redis_link(self, db_type: int = 0):
        """
        链接 redis 数据库
        :param db_type: redis 分 0-15 个数据库,区分不同 redis 缓存的数据
        :return:
        """
        if not self.redis:
            pool = redis.asyncio.ConnectionPool(
                host=setting.REDIS_HOST,
                port=setting.REDIS_PORT,
                db=db_type,
                decode_responses=True)
            self.redis = redis.asyncio.Redis(connection_pool=pool)

        return self.redis

    def cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            # 允许访问的请求地址
            allow_origins=["*"],
            # 允许跨越发送cookie
            allow_credentials=True,
            # 允许访问的请求方式，*--》 全部
            allow_methods=["*"],
            # 放行全部原始头信息
            allow_headers=["*"],
        )

    @property
    def pwd_context(self) -> CryptContext:
        """
        返回进行哈希和校验密码的对象
        """
        if not self.context:
            self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return self.context


server = Server()
