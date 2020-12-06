from api.models import Car
from rest_framework import serializers
from .model import ModelSerializer

class CarSerializer(serializers.ModelSerializer):

    model = ModelSerializer(many=False, read_only=True)
   
    class Meta:
        model = Car
        fields = ['color_type', 'doors', 'passengers', 'fuel_type', 'category','model']