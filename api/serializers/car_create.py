from api.models import Car
from rest_framework import serializers

class CarCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        exclude = ['id']