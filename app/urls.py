from fastapi import FastAPI

from app.user.urls import user_routers


def main_router(app: FastAPI):
    """
    路由管理
    """
    # 用户
    user_routers(app=app)
