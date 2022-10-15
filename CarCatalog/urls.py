from django.urls import path
from CarCatalog.views import CarList, CarCreate

urlpatterns = [
  path('', CarList.as_view(), name='car_list'),
  path('car/new/', CarCreate.as_view(), name='car_new'),
]