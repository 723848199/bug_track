from datetime import datetime, timedelta
from typing import Union

from fastapi import Cookie, Response, Depends, status
from jose import jwt
from pydantic import ValidationError

from app.user.models import User, Token
from service import HTTPException, server
from settings import setting


def verify_password(plain_password, hashed_password):
    """
    校验密码
    :param plain_password: 原密码
    :param hashed_password: 哈希后的密码
    :return: bool  校验成功返回True,反之False
    """

    # noinspection PyBroadException
    try:
        return server.pwd_context.verify(plain_password, hashed_password)
    except Exception:
        return False


def get_password_hash(password):
    """
    哈希来自用户的密码
    :param password: 原密码
    :return: 哈希后的密码
    """
    return server.pwd_context.pwd_context.hash(password)


async def check_user(account, password) -> Union[User, bool]:
    """
    校验用户密码
    :param account: 账号
    :param password: 密码
    :return:
    """
    user = await User.filter(account=account, is_delete=False).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    # if user.is_delete or user.status is not UserStatus.normal:
    #     raise HTTPException(msg='用户状态异常')
    return user


def create_access_token(data: dict, expires_delta: int = setting.ACCESS_TOKEN_EXPIRE_MINUTES):
    """
    访问令牌,创建token
    :param data: 需要JWT令牌加密的数据
    :param expires_delta: 令牌有效期
    :return: token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    # 添加失效时间
    to_encode.update({"exp": expire})
    # SECRET_KEY:密钥
    # ALGORITHM:令牌签名算法
    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    return encoded_jwt


async def check_jwt_token(token: str = Cookie(default='')) -> Union[User, None]:
    """
    验证token
    :param token: 浏览器取到的一个字符串的值
    :return: 用户
    """
    try:
        payload = jwt.decode(token, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
        account: str = payload.get('sub')
        user = await User.get_or_none(account=account)
        if not user:
            raise HTTPException(code=status.HTTP_401_UNAUTHORIZED, msg='token验证成功,用户查找失败')
        if datetime.utcnow() + timedelta(minutes=10) > datetime.utcfromtimestamp(payload.get('exp')):
            # 过期时间小于10分钟,刷新token
            access_token = create_access_token(data={'sub': user.username})
            # response.headers['token'] = access_token
            response = Response()
            response.set_cookie(key='token', value=access_token)
            await Token.update_or_create(defaults={'token': access_token}, user=user)
        return user
    except (jwt.JWTError, jwt.ExpiredSignatureError, ValidationError):
        raise HTTPException(code=status.HTTP_401_UNAUTHORIZED, msg='token验证失败')


