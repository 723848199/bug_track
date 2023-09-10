from fastapi import FastAPI

from app.bom_auto.urls import bom_auto_router
from app.user.urls import user_routers


def router(app: FastAPI):
    """
    总路由管理
    """
    # 用户
    user_routers(app=app)
    bom_auto_router(app=app)
