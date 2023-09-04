from fastapi import Depends, Path, Response, Body

from core import server
from app.user.schemas import UserOut
from app.user.auth import check_jwt_token
from app.user.models import User, Token
from common.exception import HTTPException


async def logout(response: Response, user: User = Depends(check_jwt_token)):
    response.delete_cookie(key='token')
    await Token.filter(pk=user.pk).update(token=None)
    return '操作成功'


async def user_info(user: User = Depends(check_jwt_token)):
    return await UserOut.from_tortoise_orm(user)


async def user_all():
    return await UserOut.from_queryset(User.filter(is_delete=False))


async def assign_info(user_id: int = Path(default=..., description='用户id', )):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(msg='请求的数据不存在')
    return await UserOut.from_tortoise_orm(user)


async def reset_password(user: User = Depends(check_jwt_token), new_password: str = Body()):
    new_password = server.pwd_context.hash(new_password)
    await User.filter(pk=user.pk).update(password=new_password)
    return '操作成功'


