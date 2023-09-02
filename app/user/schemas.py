# User = pydantic_model_creator(Users, )
#
#
# UserIn = pydantic_model_creator(Users, exclude_readonly=True, include=('UserStatus',))
# UserSchema = pydantic_model_creator(Users)
#
# class UserStatusSchema(pydantic_model_creator(UserStatus, include=('name',))):
#     name: str
#     pass
# class UserSchema(pydantic_model_creator(Users)):
#     status: UserStatusSchema = None
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.user.models import User


class Login(BaseModel):
    account: str
    password: str
    username: str = None
    phone: str = None

    class Config:
        from_attributes = True


UserOut = pydantic_model_creator(User)
