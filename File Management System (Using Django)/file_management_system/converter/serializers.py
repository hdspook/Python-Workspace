from rest_framework import serializers

from .models import Convert


class ConvertSerializer(serializers.ModelSerializer):
    '''
    Serializer to take just the file names as post request
    '''
    class Meta:
        model = Convert
        fields = ['file_name']

class StatusSerializer(serializers.ModelSerializer):
    '''
    Serializer to return the database object of converted files
    '''
    class Meta:
        model = Convert
        fields = '__all__'