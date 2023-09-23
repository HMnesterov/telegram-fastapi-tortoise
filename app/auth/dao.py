from tortoise import models, fields

class WebUser(models.Model):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=255, index=True, unique=True)
    hashed_password = fields.CharField(max_length=255, null=False)
    disabled = fields.BooleanField()
