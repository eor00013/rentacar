from api.serializers.car_create import CarCreateSerializer
from api.serializers import CarSerializer
from typing import List
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import json
from api.models import Car
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


# # Create your views here.
# def _create_mock_cars(toJson: bool = False):
#     class Car():
#         def __init__(self, id: int, door: int, wheels: int,brand: str, model: str, registrationId: str):
#             self.id = id
#             self.door = door
#             self.wheels = wheels
#             self.brand = brand
#             self.model = model
#             self.registrationId = registrationId

#         def toJson(self):
#             return json.dumps(self, default=lambda o: o.__dict__)

#         def __str__(self):
#             return f"Id: {self.id}, brand: {self.brand}, model: {self.model}, registrationId: {self.registrationId}"

#     porsche = Car(0, 3, 4, 'Porsche', '911', None )
#     hyundai = Car(1, 5, 4, 'Hyundai', 'i30', '345PJK' )

#     if (toJson):
#         return [porsche.toJson(), hyundai.toJson()]
#     else:
#         return [porsche, hyundai]


# def findCar (car_id: int, cars: List):
#     for car in cars:
#         if car.id == car_id:
#             return car
#     return None

# class CarViewSet(viewsets.ViewSet):
       
#     def list(self, request, format=None):
#         """
#         GET (ALL)
#         """
#         return Response({'cars': _create_mock_cars(True)}, status=status.HTTP_200_OK)
       

#     def retrieve(self, request, car_id=None):
#         """
#         GET (ONE)
#         """
#         print(car_id)
#         cars = _create_mock_cars()
#         car_to_return = findCar(car_id, cars)
#         if(car_to_return):
#             return Response({'car': car_to_return.toJson()}, status=status.HTTP_200_OK )
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)    

#     def create(self, request):
#         """
#         POST
#         """
#         cars = _create_mock_cars()
#         new_car = request.data
#         print(new_car)
#         new_car['id'] = len(cars)
#         cars.append(new_car)
#         print(cars[1])
#         return Response(new_car, status=status.HTTP_201_CREATED)

#     def find_car(self, id:int, cars:List):
#         for car in cars:
#             if (car.id == id):
#                 return car
        
#         return None
    
    
#     def update(self, request, car_id=None):
#         """
#         PUT
#         """ 
#         cars = _create_mock_cars()
#         car_to_return = self.find_car(car_id, cars)
#         if(car_to_return):
#             car_updated = request.data

#             # DIRTY VERSION
#             # if('doors' in car_updated):
#             #     car_to_return.doors = car_updated.doors
#             # if('wheels' in car_updated):
#             #     car_to_return.wheels = car_updated.wheels
#             # if('brand' in car_updated):
#             #     car_to_return.brand = car_updated.brand
#             # if('model' in car_updated):
#             #     car_to_return.model = car_updated.model
#             # if('resgistrationId' in car_updated):
#             #     car_to_return.resgistrationIds = car_updated.resgistrationId
            

#              # CLEAN VERSION

#             for key in car_updated:
#                  if(getattr(car_to_return, key)):
#                      setattr(car_to_return, key, car_updated[key])
#             return Response({'car': car_to_return.toJson()}, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def destroy(self, request, car_id=None):
#         """
#         DELETE
#         """ 
#         cars = _create_mock_cars()
#         for car in cars:
#             if car.id == id:
#                 cars.remove(car)
#                 print("I found it!")
#                 return Response({'car': car.toJson()}, status=status.HTTP_200_OK)
#             return Response("Item not found",status=status.HTTP_404_NOT_FOUND)

####################  DATA BASE(DB/DBB) VERSION ####################

class CarViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        GET (ALL)
        """
        cars_db = Car.objects.all()

        cars_serializer = CarSerializer(cars_db, many=True)
        return Response(cars_serializer.data)

    def retrieve(self, request, car_id=None):
        """
        GET (ONE)
        """
        # DIRTY VERSION
        # cars_db = Car.objects.all()
        # car = get_object_or_404(cars_db, pk=car_id)
        
        # CLEAN VERSION
        car = get_object_or_404(Car, pk=car_id)

        car_serializer = CarSerializer(car)
        return Response(car_serializer.data)

    @swagger_auto_schema(request_body=CarCreateSerializer)
    def create(self, request):
        """
        POST
        """
        car_serializer = CarCreateSerializer(data=request.data, context={'request' : request})

        if car_serializer.is_valid():
            car_serializer.save()
            return Response(car_serializer.data, status=status.HTTP_201_CREATED)
        return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=CarCreateSerializer)
    def update(self, request, car_id=None):
        """
        PUT
        """ 
        # DIRTY VERSION
        # cars_db = Car.objects.all()
        # car = get_object_or_404(cars_db, pk=car_id)
        
        # CLEAN VERSION
        car = get_object_or_404(Car, pk=car_id)
        
        car_serializer = CarCreateSerializer(car, data=request.data, partial=True)

        if car_serializer.is_valid():
            car_serializer.save()
            return Response(car_serializer.data, status=status.HTTP_200_OK)
        return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, car_id=None):
        """
        DELETE
        """ 
        # DIRTY VERSION
        # cars_db = Car.objects.all()
        # car = get_object_or_404(cars_db, pk=car_id)
        
        # CLEAN VERSION
        car = get_object_or_404(Car, pk=car_id)
        car.delete()

        car_serializer = CarSerializer(car)

        return Response(car_serializer.data, status=status.HTTP_200_OK)
