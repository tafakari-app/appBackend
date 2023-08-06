from .models import Journal
from rest_framework import serializers



class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

class CreateJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ("title","description")
