from rest_framework import status
from retriever.models import Retrieve
from retriever.serializers import RetrieveSerializer
from .helpers.create_and_save import create
from rest_framework.views import APIView
from rest_framework.response import Response
import os

# Create your views here.
class SplitAndSave(APIView):
    """
    Retrieve patient detail from db and save to word and xlsx file
    """
    def get(self,request):
        #query db and return object
        query_file_set = Retrieve.objects.all()
        serializer = RetrieveSerializer(query_file_set, many=True, context={'request':request})
        create(serializer.data)
        return Response(serializer.data)