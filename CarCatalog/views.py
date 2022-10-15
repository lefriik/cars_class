from django.shortcuts import render, redirect

from django.views import View


from .models import Car
from .forms import CarForm


# Django Class-Based Views
class CarList(View): 
  

  def get(self, request, *args, **kwargs): 
    car_list = Car.objects.all()
    template_name = 'CarCatalog/car_list.html' 
    return render(request, template_name, {'car_list': car_list} ) 


class CarCreate(View): 
  
  form_class = CarForm 

  def get(self, request, *args, **kwargs): 
    form = self.form_class 
    template_name = 'CarCatalog/car_edit.html' 
    return render(request, template_name, {'form': form })

  def post(self, request, *args, **kwargs): 
    
    template_name = 'CarCatalog/car_edit.html' 
    form = self.form_class(request.POST) 
    if form.is_valid():
      car = form.save(commit=False)
      car.save()
      return redirect('car_list')
    return render(request, template_name, {'form': form })


# Django Generic Class-Based Views