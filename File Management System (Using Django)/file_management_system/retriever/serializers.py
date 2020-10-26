from rest_framework import serializers

from .models import Retrieve

class RetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retrieve
        fields = '__all__'

class FileHandlerSerializer(serializers.Serializer):
    file_name = serializers.CharField(max_length=200)