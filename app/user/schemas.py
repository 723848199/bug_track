from tortoise.contrib.pydantic import pydantic_model_creator
from app.user.models import User

# 序列化登录模型,仅验证固定字段
Login = pydantic_model_creator(User, name='login', include=('account', 'password', 'username', 'phone'))
# 序列化用户返回模型,返回数据中排除 password
UserOut = pydantic_model_creator(User, name='user_out', exclude=('password',))
