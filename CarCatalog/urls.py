from django.urls import path
from CarCatalog.views import CarList

urlpatterns = [
  path('', CarList.as_view(), name='car_list'),
]