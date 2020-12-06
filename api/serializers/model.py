from api.models import  Model
from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = ['name']