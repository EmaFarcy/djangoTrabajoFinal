from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Cicloturista(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    contado= models.BooleanField()
    
    def __str__(self):
        return f' {self.nombre} {self.apellido}'
    
    
class Corredor(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    equipo= models.CharField(max_length=60)
    
    def __str__(self):
        return f' {self.nombre} {self.apellido}'

class Ruta(models.Model):
     marca = models.CharField(max_length=60)
     modelo = models.CharField(max_length=60)
     caracteristicas= RichTextField(blank=True, null=True)
     imagen_ruta = models.ImageField(upload_to='bikes/', blank= True, null= True)
     fecha_creacion = models.DateTimeField(default=timezone.now)
     
     def __str__(self):
        return f' {self.marca} {self.modelo}'

class Mtb(models.Model):
     marca = models.CharField(max_length=60)
     modelo = models.CharField(max_length=60)
     caracteristicas= RichTextField(blank=True, null=True)
     imagen_mtb = models.ImageField(blank= True, null= True)
     fecha_creacion = models.DateTimeField(default=timezone.now)
     
     def __str__(self):
        return f' {self.marca} {self.modelo}'
    
class Urbana(models.Model):
     marca = models.CharField(max_length=60)
     modelo = models.CharField(max_length=60)
     caracteristicas= RichTextField(blank=True, null=True)
     imagen_urbana = models.ImageField(blank= True, null= True)
     fecha_creacion = models.DateTimeField(default=timezone.now)
     
     def __str__(self):
        return f' {self.marca} {self.modelo}'      