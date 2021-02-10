from rest_framework import viewsets
from rest_framework.response import Response
from api.models import City
from api.serializers import CitySerializer


class LocationsViewSet(viewsets.ViewSet): 
     def list(self, request):
        """
        GET (ALL)
        """
        cities_db = City.objects.all()

        cities_serializer = CitySerializer(cities_db,many=True)

        locations = cities_serializer.data

        return Response(locations)

