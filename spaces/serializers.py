from rest_framework import serializers
from .models import Post, PostComment
from users.serializers import MyuserSerializer

class PostCommentSerializer(serializers.ModelSerializer):
    author = MyuserSerializer(read_only=True)
    class Meta:
        model = PostComment
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    comments = PostCommentSerializer(many=True)
    author = MyuserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"


class CreateNewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "description")
