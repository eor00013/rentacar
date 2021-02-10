from api.serializers.brand import BrandSerializer
from api.models import  Model
from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    class Meta:
        model = Model
        fields = ['name', 'brand', 'photo']