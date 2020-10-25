from rest_framework import status
from .serializers import ConvertSerializer
from .models import Convert
from rest_framework.views import APIView
from rest_framework.response import Response
import os

from .helpers.get_file_url import file_url_list
from .helpers.convert_helper import start_converting

# Create your views here.

class ConvertAndSave(APIView):
    """
    Convert multiple file formats to pdf
    """
    def get(self,request):
        #query db and return object
        query_file_set = Convert.objects.all()
        serializer = ConvertSerializer(query_file_set, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConvertSerializer(data=request.data)
        if serializer.is_valid():
            #get file url to convert
            file_url = file_url_list(serializer.validated_data.get('file_name'))
            #call the helper function to convert
            start_converting(file_url[0], serializer.validated_data.get('output_file_name'))
            #save the results
            serializer.save()
            #return response
            return Response("File Successfully Converted", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
