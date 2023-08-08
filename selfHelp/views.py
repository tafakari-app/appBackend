from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
import json
from rest_framework import status
from .models import Library
from .serializers import LibrarySerializer
from rest_framework.parsers import FormParser


class LibraryView(APIView):
    serializer_class = LibrarySerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (FormParser,)

    def get(self, request):
        try:
            featured = Library.objects.all().filter(is_featured=True).first()
            queryset = Library.objects.all()
            serializer = LibrarySerializer(queryset, many=True)
            response_data = {
                "featured": LibrarySerializer(featured).data if featured else None,
                "videos": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except:
            return Response({"Message": "Error"}, status=status.HTTP_404_NOT_FOUND)
