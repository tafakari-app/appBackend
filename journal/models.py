from django.db import models
from django.urls import reverse
from users.models import MyUser
import uuid

class Journal(models.Model):
    ID = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="journals")
    title = models.CharField(max_length=100, blank=True, null=True)
    emotion = models.CharField(max_length=100, blank=True, null=True)
    emotion_predications = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Journal"
        verbose_name_plural = "Journals"
        ordering = ("-created_at", )

    def __str__(self):
        return self.title
