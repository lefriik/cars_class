from django.shortcuts import render
from django.views import View

from .models import Car


# Create your views here.

class CarList(View):
  

  def get(self, request, *args, **kwargs):
    template_name = 'CarCatalog/car_list.html'
    car_list = Car.objects.all()
    
    return render(request, template_name, {'car_list': car_list})

  


