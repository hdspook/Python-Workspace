from rest_framework import status
from .serializers import RetrieveSerializer, FileHandlerSerializer
from .models import Retrieve
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from .helpers.get_file_url import file_url_list
from .helpers.read_file import readFile

# Create your views here.

class RetrieveAndSave(APIView):
    """
    Retrieve patient detail from file and save to db
    """
    def get(self,request):
        #query db and return object
        query_file_set = Retrieve.objects.all()
        serializer = RetrieveSerializer(query_file_set, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FileHandlerSerializer(data=request.data)
        if serializer.is_valid():
            #get file url to convert
            file_url = file_url_list(serializer.validated_data.get('file_name'))
            #call the helper function to read file data
            line = readFile(file_url[0]).split(",")
            #Save data to database
            query_file_set = Retrieve.objects.create(name = line[0], email = line[1], age = line[2])
            #return the response
            return Response("File Successfully Retrieved", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
