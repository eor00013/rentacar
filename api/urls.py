from api import views
from django.urls import path

car_list = views.CarViewSet.as_view({'get': 'list', 'post': 'create'})
car_detail =  views.CarViewSet.as_view({'get': 'retrieve', 'put' : 'update', 'delete' : 'destroy'})
urlpatterns = [
    path('cars/', car_list, name='card-list'),
    path('cars/<int:car_id>/', car_detail, name='car-detail'),
]