
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
from .models import MyUser


class MyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'fullname')

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'fullname',
                  'password')
