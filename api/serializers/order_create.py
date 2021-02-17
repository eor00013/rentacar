from api.models import Order
from rest_framework import serializers

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ['id', 'user', 'created_at','updated_at']