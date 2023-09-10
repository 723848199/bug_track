from fastapi import FastAPI

from app.user.urls import user_routers


def router(app: FastAPI):
    """
    总路由管理
    """
    # 用户
    user_routers(app=app)
