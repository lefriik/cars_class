from django.urls import path
#from CarCatalog.views import CarList, CarCreate
from CarCatalog.views import  CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
  #path('', CarList.as_view(), name='car_list'),
  #path('car/new/', CarCreate.as_view(), name='car_new'),
  path('', CarListView.as_view(), name='car_list'),
  path('car/create/', CarCreateView.as_view(), name='car_create'),
  path('car/<int:pk>/detail', CarDetailView.as_view(), name='car_detail'),
  path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
  path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]