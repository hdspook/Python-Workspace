from rest_framework import status
from .serializers import ConvertSerializer, StatusSerializer
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
        serializer = StatusSerializer(query_file_set, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConvertSerializer(data=request.data)
        if serializer.is_valid():
            #get file url to convert
            file_url = file_url_list(serializer.validated_data.get('file_name'))
            #call the helper function to convert
            file_info = start_converting(file_url[0])
            if file_info is not None:
                query_file_set = Convert.objects.create(file_name = serializer.validated_data.get('file_name')
                                                        , output_file_name = file_info[0]
                                                        , output_file_path = file_info[1]
                                                        , convert_status = file_info[2])
            else:
                raise TypeError
            
            #save the results
            #serializer.save()
            serializer = StatusSerializer(query_file_set)
            #return response
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
