from fastapi import Body, Depends, Response, Request
from fastapi.security import OAuth2PasswordRequestForm

from app.user.auth import verify_password, create_access_token
from app.user.models import User, Token
from app.user.schemas import Login, UserOut
from service import HTTPException, server, SMS
from service.utils.tools import code_number


async def register(req: Request, user: Login = Body(), code: str = Body(default=None),
                   ):
    if await User.get_or_none(account=user.account):
        raise HTTPException(msg=f'{user.account} 用户已存在')
    if user.phone:
        # 注册阶段如果提供手机号,需对手机号进行判断,
        if await User.get_or_none(phone=user.phone):
            raise HTTPException(msg=f'{user.phone} 手机号已绑定')
        else:
            data = req.state.check.getdel(name=f"{user.phone}__1")
            print(code, data, type(code), type(data))
            if not data == code:
                raise HTTPException(msg='验证码不正确')
            print(data)
    user.password = server.pwd_context.hash(user.password)
    user_obj = await User.create(**user.model_dump())
    return await UserOut.from_tortoise_orm(user_obj)


async def login(user_data: OAuth2PasswordRequestForm = Depends()):
    if user_obj := await User.get_or_none(account=user_data.username, is_delete=False):

        if verify_password(user_data.password, user_obj.password):
            # 创建token
            access_token = create_access_token(data={'sub': user_obj.account})
            await Token.update_or_create(defaults={'token': access_token}, user=user_obj)
            # 将token写入到浏览器cookie中
            response = Response()
            response.set_cookie(key='token', value=access_token)
            return response
        else:
            raise HTTPException(msg='用户名或密码错误')
    else:
        raise HTTPException(msg='账号不存在或已注销')


async def send_sms(request: Request, phone: int = Body(default=...), code_type: int = Body(default=1)):
    """
    :param request:
    :param phone: 手机号
    :param code_type: 类型 1,注册账号
    :return:
    """
    if code := await request.app.state.check.get(f"{phone}__{code_type}"):
        print(code)
        raise HTTPException(msg='验证码已发送,稍后再试')

    code = code_number(length=6)
    print(code)
    await SMS.send_code(phone=phone, code_type=code_type, code=code)

    await request.app.state.check.set(f"{phone}__{code_type}", code, ex=60 * 5)
    return '短信发送成功'
