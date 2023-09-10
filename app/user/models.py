from tortoise import fields, Model
from app.models import Abstract


class User(Abstract):
    account = fields.CharField(max_length=50, index=True, unique=True, description='账号', null=True)
    username = fields.CharField(max_length=50, description='用户名', null=True, default=None)
    password = fields.CharField(max_length=100, index=True, description='密码')
    phone = fields.CharField(max_length=15, index=True, description='手机号', null=True, default=None)

    # 不生产实际字段,仅作为编辑器代码提示
    token: fields.ReverseRelation["Token"]
    group: fields.ReverseRelation["UserGroup"]

    class Meta:
        table = 'users'

    class PydanticMeta:
        exclude = ['password']


class UserGroup(Abstract):
    name = fields.CharField(max_length=50, description='用户组名称')
    user: fields.ForeignKeyNullableRelation[User] = fields.ForeignKeyField('User.User', related_name='user',
                                                                            )


class Token(Model):
    user: fields.ForeignKeyNullableRelation[User] = fields.ForeignKeyField('User.User', related_name='token',
                                                                           null=True)
    token = fields.CharField(max_length=255, null=True)


from enum import IntEnum


class Gender(IntEnum):
    man = 1
    woman = 2
    secrecy = 0


class UserModel(Abstract):
    """
    ipynb测试模型
    """
    account = fields.CharField(max_length=50, index=True, description='账号', null=True)
    password = fields.CharField(max_length=100, index=True, description='密码')
    gender = fields.IntEnumField(enum_type=Gender, defalut=Gender.secrecy.value, )
    integral = fields.DecimalField(max_digits=10, decimal_places=5, null=True, default=None)


class Class(Model):
    name = fields.CharField(max_length=40)


class Student(Model):
    name = fields.CharField(max_length=30)
    my_class: fields.ForeignKeyRelation[Class] = fields.ForeignKeyField('User.Class', related_name='students')
