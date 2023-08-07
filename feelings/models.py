from django.db import models
from users.models import MyUser
import uuid


class Feelings(models.Model):
    ID = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="feelings")
    emotion = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Feelings"
        verbose_name_plural = "Feelings"

    def __str__(self):
        return self.emotion
    



