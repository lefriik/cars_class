
from django.db import models

# Create your models here.
class Car(models.Model):
  plate = models.CharField(max_length = 8, unique = True)
  brand = models.CharField(max_length = 25)
  color = models.CharField(max_length = 30)