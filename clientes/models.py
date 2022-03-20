from django.db import models

# Create your models here.

class Cicloturista(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    contado= models.BooleanField()
    
class Corredor(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    equipo= models.CharField(max_length=60)