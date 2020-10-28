from rest_framework import serializers

from .models import Merge


class MergeSerializer(serializers.ModelSerializer):
    '''
    Serializer to take just the file names as post request
    '''
    class Meta:
        model = Merge
        fields = ['file_names']

class StatusSerializer(serializers.ModelSerializer):
    '''
    Serializer to return the database object of merged files
    
    '''
    class Meta:
        model = Merge
        fields = '__all__'