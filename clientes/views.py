from django.shortcuts import render
from .models import Cicloturista, Corredor, Ruta
from .forms import CicloturistaFormulario, CicloturistaBusqueda, CorredorFormulario, CorredorBusqueda, RutaFormulario

def crear_cicloturista(request):
    
    if request.method=='POST':
        form= CicloturistaFormulario(request.POST)
        
        if form.is_valid():
            data= form.cleaned_data
            cicloturista= Cicloturista(nombre= data['nombre'], apellido=data['apellido'], contado= data['contado']) 
            cicloturista.save()
            return render(request, "index/nosotros.html", {})
        
    form= CicloturistaFormulario()
    return render (request, "clientes/crear_cicloturista.html", {'form': form})

def lista_cicloturistas(request):
    
    nombre_a_buscar= request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        cicloturistas = Cicloturista.objects.filter(nombre__icontains= nombre_a_buscar)
    else: 
        cicloturistas = Cicloturista.objects.all()
     
    form= CicloturistaBusqueda()
    return render(request, "clientes/lista_cicloturistas.html", {'form': form, "cicloturistas": cicloturistas})


def crear_corredor(request):
    
    if request.method=='POST':
        form= CorredorFormulario(request.POST)
        
        if form.is_valid():
            data= form.cleaned_data
            corredor= Corredor(nombre= data['nombre'], apellido=data['apellido'], equipo= data['equipo']) 
            corredor.save()
            return render(request, "index/nosotros.html", {})
        
    form= CorredorFormulario()
    return render (request, "clientes/crear_corredor.html", {'form': form})

def lista_corredores(request):
    
    nombre_a_buscar= request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        corredores = Corredor.objects.filter(nombre__icontains= nombre_a_buscar)
    else: 
        corredores = Corredor.objects.all()
     
    form= CorredorBusqueda()
    return render(request, "clientes/lista_corredores.html", {'form': form, "corredores": corredores})

def crear_ruta(request):
    if request.method=='POST':
        form= RutaFormulario(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            ruta= Ruta(marca= data['marca'], modelo=data['modelo'])
            ruta.save()
            return render(request, "index/index.html", {})
    form= RutaFormulario()
    return render(request, "clientes/crear_ruta.html", {'form': form})