from fastapi import Body, Depends, Response, Request
from fastapi.security import OAuth2PasswordRequestForm

from app.user.auth import verify_password, create_access_token
from app.user.models import User, Token
from app.user.schemas import Login, UserOut
from service import HTTPException, server, SMS
from service.utils.tools import code_number


async def register(request: Request, user: Login = Body(), code: str = Body(default=None)):
    """
    request:  接口请求的所有数据.请求地址,请求方法,请求内容.等
    user: 注册的数据内容格式
    code: 注册所需验证码
    """
    # get_or_none() 根据参数从数据库获取一条数据,如果没获取到返回 None
    if await User.get_or_none(account=user.account):
        # 如果用户存在 主动抛出异常
        raise HTTPException(msg=f'{user.account} 用户已存在')
    if user.phone:
        # 注册阶段如果提供手机号,需对手机号进行判断,
        if await User.get_or_none(phone=user.phone):
            raise HTTPException(msg=f'{user.phone} 手机号已绑定')
        else:
            """
            从 redis 数据库获取验证码的值,
            app.state.check   redis数据库对象
            getdel 获取后删除数据
            name=f"{user.phone}__1"  从 redis 中获取一个名称为  user.phone__1 的值
            """
            data = await request.app.state.check.getdel(f"{user.phone}__1")

            print(code, data, type(code), type(data))
            """
            data :从 redis 数据库中获取到的验证码数据
            code: 前端调用 api 穿的参数
            如果两个值相等,证明验证码通过
            """
            if not data == code:
                raise HTTPException(msg='验证码不正确')
            print(data)
    """
    对前端获取到的密码进行加密处理,
    """
    user.password = server.pwd_context.hash(user.password)
    """
    create 往数据库中插入一条数据,
    ** 解包,讲字典对象的数据一一解包传输给 create
    user.model_dump()   将获取到的 user 转换成字典格式
    """
    user_obj = await User.create(**user.model_dump())
    """
    UserOut 返回数据的序列化模型
    from_tortoise_orm()  将一条数据对象序列化 
    """
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
    """
    发送验证码前先查询 ,看是否已发送,如果验证码还没失效,不重复发送
    """
    if code := await request.app.state.check.get(f"{phone}__{code_type}"):
        print(code)
        raise HTTPException(msg='验证码已发送,稍后再试')

    # 获取六位数随机验证码
    code = code_number(length=6)
    print(code)
    # 调用阿里云短信服务,发送验证码
    await SMS.send_code(phone=phone, code_type=code_type, code=code)
    # 验证码发送成功,写入 redis 数据库
    await request.app.state.check.set(f"{phone}__{code_type}", code, ex=60 * 5)
    return '短信发送成功'


"""
tortoise orm 简易使用方式 以 User 表举例

await User.all()  获取 User 表中所有数据
await User.get(id  = 1) 获取 User 表中 id 为1 的数据,如果不存在,报错
await User.get_or_none(id = 1) 获取 User 中 id 为 1 的数据,如果数据不存在,返回 None
await User.filter(age = '男') 查询 User 中 性别 为 男 的数据,查询到的是一个列表,如果没查询到数据,返回空列表
await User.filter(app= '男').first(),返回获取到的第一个对象
await User.filter(name='arya').delete() 删除查询到的数据对象
await User.filter(name='arya').update(name='arya001') 批量更新数据

user = await User.filter(name='arya').first()
user.name = 'name001'  更新一条数据
user.save()     保存更新

await User.create(**)  根据参数新建一条数据

user.delete()


"""
