from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.generics import GenericAPIView
from .models import (
    Post
)
from rest_framework.pagination import PageNumberPagination

from rest_framework import permissions
import json
from rest_framework import status
from .serializers import (
    PostSerializer, CreateNewPostSerializer
)
from django_filters import rest_framework as filters
from .filters import PostFilter
from .Predictions import predictEmtions
from rest_framework import generics


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 100


class Feeds(generics.ListAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter
    permission_classes = (permissions.IsAuthenticated,)
    # Use your custom pagination class if needed
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Post.objects.all()

    def get(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Message": "Error"}, status=status.HTTP_404_NOT_FOUND)


class FeedsDetails(APIView):
    parser_classes = (MultiPartParser,)
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        try:
            queryset = Post.objects.get(ID=pk)
            serializer = self.serializer_class(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Message": "Error"}, status=status.HTTP_404_NOT_FOUND)


class CreatePost(APIView):
    parser_classes = (MultiPartParser,)
    serializer_class = CreateNewPostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body)
        try:
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                post = serializer.save(author=request.user)
                post_serializer = PostSerializer(instance=post)

                return Response(post_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"Message": "Sorry we have an Error! "}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Error": "Sorry we can't post "}, status=status.HTTP_400_BAD_REQUEST)


class LikePost(APIView):
    parser_classes = (MultiPartParser,)
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, post_id):
        try:
            post = Post.objects.get(ID=post_id)
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
            serializer = PostSerializer(instance=post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"Message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"Error": "Error liking/disliking post"}, status=status.HTTP_400_BAD_REQUEST)
