from rest_framework import viewsets, status
from api.serializers import OrderCreateSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class OrdeViewSet(viewsets.ViewSet):        
    @swagger_auto_schema(request_body=OrderCreateSerializer) 
     def create(self, request):
        """
         POST
        """
        order_serializer = OrderCreateSerializer(
            data=request.data, context={'request': request})
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors,status=status.HTTP_400_BAD_REQUEST )