from django.shortcuts import render

from .models import Car


# Create your views here.

class CarList():
  

  def get(self, request, *args, **kwargs):
    template_name = 'CarCatalog/car_list.html'
    cars = Car.objects.all()
   
    return render(request, template_name, {'cars': cars})

  


