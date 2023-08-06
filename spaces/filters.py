from django_filters.rest_framework import FilterSet, filters
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title':['exact', 'contains'],
            'description':['exact', 'contains'],
        }
