from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

# ------ Django Class-Based Views -------

from django.views import View 
from django.urls import reverse_lazy


# ------ Django Generic Class-Based Views --------

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


#----------------------------------------------------------------------------------------
# Django Class-Based Views
"""   
class CarList(View): 
  

  def get(self, request, *args, **kwargs): 
    car_list = Car.objects.all()
    template_name = 'CarCatalog/car_list.html' 
    return render(request, template_name, {'car_list': car_list} ) 


class CarCreate(View): 
  
  form_class = CarForm 

  def get(self, request, *args, **kwargs): 
    # *args param opcional donde pasas la cantidad que necesites sin limite
    # **kwargs param opcion donde pasas la cantidad que necesites con nombres
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

"""


#----------------------------------------------------------------------------------------


# Django Generic Class-Based Views

class CarView(View):
    model = Car
    fields = '__all__'   
    success_url = reverse_lazy('car_list')

class CarListView(CarView, ListView):
    """View para listar los autos"""

class CarDetailView(CarView, DetailView):
    """View para listar detalles de autos"""

class CarCreateView(CarView, CreateView):
  """View para crear un auto"""

class CarUpdateView(CarView, UpdateView):
    """View para actualizar un auto"""

class CarDeleteView(CarView, DeleteView):
    """View para eliminar un auto"""