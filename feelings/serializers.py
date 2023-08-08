from .models import Feelings
from rest_framework import serializers


class CreateFeelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feelings
        fields =  ('emotion',)


class FeelingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feelings
        fields = "__all__"
