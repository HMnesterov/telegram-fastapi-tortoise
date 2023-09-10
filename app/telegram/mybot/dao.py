from tortoise import models, fields


class TGMessage(models.Model):
    """Telegram message dao"""
    true_id = fields.UUIDField(pk=True, description="Database Unique ID")
    id = fields.BigIntField(description="telegram message_id", generated=False)
    author = fields.ForeignKeyField("models.TGUser", on_delete=fields.CASCADE, related_name="messages")
    chat = fields.ForeignKeyField("models.TGChat", on_delete=fields.CASCADE, related_name="chats")
    text = fields.CharField(max_length=999)
    created_at = fields.DatetimeField(description="When message was created")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Message {self.true_id}"


class TGChat(models.Model):
    """Telegram chat dao"""
    id = fields.BigIntField(pk=True, generated=False, description="telegram chat_id")
    hash = fields.CharField(max_length=999)
    full_name = fields.CharField(max_length=255)
    type = fields.CharField(max_length=255, description="Chat mode", null=True)

    def __str__(self):
        return f"Chat {self.id}"


class TGUser(models.Model):
    """Telegram user dao"""
    id = fields.BigIntField(pk=True, generated=False, description="telegram user id")
    hash = fields.CharField(max_length=999, description="To check when we need update user data")
    first_name = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, null=True)
    language_code = fields.CharField(max_length=255, null=True)

    is_bot = fields.BooleanField()

    def __str__(self):
        return f"User {self.first_name}"
