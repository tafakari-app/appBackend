from .models import Library
from rest_framework import serializers

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id','title','author','description','is_featured','link','created_at','update_at')
