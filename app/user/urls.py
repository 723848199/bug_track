from typing import List, Union

from fastapi import FastAPI, APIRouter

from app.user.api.login import *
from app.user.api.user import *
from app.user.auth import check_jwt_token

# 登录路由--不需要验证token
login_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

# 用户路由--需要验证token-登录后可以访问
user_router = APIRouter(
    dependencies=[Depends(check_jwt_token)],
    responses={404: {"description": "Not found"}},
)


def user_routers(app: FastAPI):
    app.include_router(login_router, tags=['登录'])
    app.include_router(user_router, prefix='/user', tags=['用户'])


login_router.post('/register', summary='用户注册', response_model=UserOut)(register)
login_router.post('/login', summary='用户登录')(login)
login_router.post('/send_sms', summary='获取验证码')(send_sms)

user_router.delete('/logout', summary='退出登录')(logout)
user_router.get('/me', summary='获取个人信息', response_model=UserOut)(user_info)
user_router.get('/all', summary='获取所有用户信息', response_model=List[UserOut])(user_all)
user_router.get('/{user_id}', summary='获取指定用户信息', response_model=Union[UserOut])(assign_info)
user_router.put('/me', summary='重置密码')(reset_password)
