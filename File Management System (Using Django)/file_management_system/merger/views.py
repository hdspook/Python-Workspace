from rest_framework import status
from .serializers import MergeSerializer
from .models import Merge
from .helpers.file_name_split_helper import file_url_list
from .helpers.merge_helper import merge_pdfs
from rest_framework.views import APIView
from rest_framework.response import Response
import os

class MergeAndSave(APIView):
    """
    Merges a list of pdfs
    """
    def get(self,request):
        #query db and return object
        query_file_set = Merge.objects.all()
        serializer = MergeSerializer(query_file_set, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MergeSerializer(data=request.data)
        if serializer.is_valid():
            #get url of the files
            file_list = file_url_list(serializer.validated_data.get('file_names'))
            #call merge function in helper class
            merge_pdfs(file_list, serializer.validated_data.get('output_file_name'))
            #save the results
            serializer.save()
            #return response
            return Response("File Successfully Merged", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

