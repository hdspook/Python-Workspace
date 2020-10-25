from rest_framework import serializers

from .models import Merge

class MergeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merge
        fields = '__all__'