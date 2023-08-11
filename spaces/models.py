from django.db import models
import uuid
from users.models import MyUser



class PostComment(models.Model):
    ID = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
    comment = models.TextField()
    author  = models.ForeignKey(MyUser,
                              on_delete=models.CASCADE, related_name='user_comments')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.comment



class Post(models.Model):
    ID = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
    description = models.TextField()
    author  = models.ForeignKey(MyUser,
                              on_delete=models.CASCADE, related_name='comments')
    comments = models.ManyToManyField(PostComment, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    likes = models.ManyToManyField(MyUser, related_name='post_like', null=True, blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.author.fullname


