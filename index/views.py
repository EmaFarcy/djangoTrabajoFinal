from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a mi proyecto final</h1>')

def nosotros(request):
    
    template= loader.get_template('nosotros.html')
    
    plantilla_generada = template.render({})
    
    return HttpResponse(plantilla_generada)
