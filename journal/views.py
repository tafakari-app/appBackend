from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
import json
from rest_framework import status
from .serializers import JournalSerializer, CreateJournalSerializer
from .models import Journal
from rest_framework.parsers import FormParser
from .predictEmtions import predictEmtions


class JournalsAPiView(APIView):
    serializer_class = JournalSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (FormParser,)

    def get(self, request):
        try:
            queryset = Journal.objects.all().filter(author=request.user)
            serializer = JournalSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Message": "Error"}, status=status.HTTP_404_NOT_FOUND)



class CreateJournal(APIView):
    parser_classes = (MultiPartParser,)
    serializer_class = CreateJournalSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body)
        try:
            serializer = CreateJournalSerializer(data=data)
            text_data = data.get('description')
            predi = predictEmtions(text_data)
            # print(predi)
            # print(data['description'])
            if serializer.is_valid():
                emotion = predi[0]['predictions'][0]['prediction']
                emotions_strength = predi[0]['predictions'][0]['probability'] * 100
                serializer.save(author=request.user, emotion=emotion,emotion_predications= emotions_strength)
                return Response({"Message":"a post was created"}, status=status.HTTP_201_CREATED)
            return Response({"Message":"a post was not created"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Message":"Error created"}, status=status.HTTP_400_BAD_REQUEST)


class getJournalDetials(APIView):
    parser_classes = (MultiPartParser,)
    serializer_class = JournalSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        try:
            queryset = Journal.objects.get(ID=pk)
            serializer = self.serializer_class(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Message": "Error"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)
        try:
            serializer = CreateJournalSerializer(data=data, instance=Journal.objects.get(ID=pk), partial=True)
            text_data = data.get('description')
            predi = predictEmtions(text_data)
            # print(data['description'])
            if serializer.is_valid():
                emotion = predi[0]['predictions'][0]['prediction']
                emotions_strength = predi[0]['predictions'][0]['probability'] * 100
                serializer.save(author=request.user, emotion=emotion,emotion_predications= emotions_strength)
                return Response({"Message":"Journal Updated Successfully"}, status=status.HTTP_201_CREATED)
            return Response({"Message":"a Journal  was not created"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Message":"Sorry we have an Error "}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            Journal.objects.get(ID=pk).delete()
            return Response({"Message":"Journal Deleted Successfully"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"Message":"Sorry we have an Error "}, status=status.HTTP_400_BAD_REQUEST)
