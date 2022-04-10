from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')

def clientes(request):
    return render(request, 'index/clientes.html')

def about_us(request):
    return render(request, 'index/about_us.html')

def bike_shop(request):
    return render(request, 'index/bike_shop.html')
