from tortoise import fields, Model


class Abstract(Model):
    is_delete = fields.BooleanField(default=False, null=True, description='是否删除')
    created = fields.DatetimeField(null=True, auto_now_add=True, description='创建时间')
    modified = fields.DatetimeField(null=True, auto_now=True, description='最后修改时间')

    class Meta:
        abstract = True
