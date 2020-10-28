from rest_framework import status
from .serializers import MergeSerializer, StatusSerializer
from .models import Merge
from .helpers.file_name_split_helper import file_url_list
from .helpers.merge_helper import merge_pdfs
from rest_framework.views import APIView
from rest_framework.response import Response
import os

class MergeAndSave(APIView):
    """
    Merges a list of pdfs based on the request
    """
    def get(self,request):
        #query db and return object
        query_file_set = Merge.objects.all()
        serializer = StatusSerializer(query_file_set, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MergeSerializer(data=request.data)
        if serializer.is_valid():
            #get url of the files
            file_list = file_url_list(serializer.validated_data.get('file_names'))
            #call merge function in helper class
            file_info = merge_pdfs(file_list)
            query_file_set = Merge.objects.create(file_names = serializer.validated_data.get('file_names')
                                                    , output_file_name = file_info[0]
                                                    , output_file_path = file_info[1]
                                                    , merge_status = file_info[2])
            #save the results
            #serializer.save()
            serializer = StatusSerializer(query_file_set)
            #return response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

