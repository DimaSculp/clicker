from tortoise import fields
from tortoise.models import Model

class User (Model):
    id = fields.BigIntField(True)
    clicks = fields.IntField()