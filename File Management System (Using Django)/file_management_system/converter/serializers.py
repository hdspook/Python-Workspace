from rest_framework import serializers

from .models import Convert

class ConvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convert
        fields = '__all__'