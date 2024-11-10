from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=150)
    email = fields.CharField(max_length=255, unique=True, db_index=True)
    password = fields.CharField(max_length=100)
    is_active = fields.BooleanField(default=False)
    verified_at = fields.DatetimeField(null=True, default=None)
    updated_at = fields.DatetimeField(null=True, default=None, auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"

    class PydanticMeta:
        exclude = ["password"]
