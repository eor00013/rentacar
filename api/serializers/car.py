from api.models import Car
from rest_framework import serializers
from .model import ModelSerializer
from .category import CategorySerializer


class CarSerializer(serializers.ModelSerializer):

    model = ModelSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)   
    class Meta:
        model = Car
        fields = ['id', 'color_type', 'doors', 'passengers', 'fuel_type', 'category','model']