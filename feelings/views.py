from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
import json
from rest_framework import status
from rest_framework.parsers import FormParser
from .models import Feelings
from .serializers import FeelingsSerializer


class FeelingsAPIView(APIView):
    serializer_class = FeelingsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (FormParser,)

    def post(self, request):
        data = json.loads(request.body)

        try:
            serializer = FeelingsSerializer(data=data)

            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response({"Message":"Emotion Registered"}, status=status.HTTP_201_CREATED)
            return Response({"Message":"Emotion Not Registered"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Message":"Sorry couldn't Register Emotion"}, status=status.HTTP_400_BAD_REQUEST)


