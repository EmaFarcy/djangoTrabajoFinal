from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')

def nosotros(request):
    return render(request, 'index/nosotros.html')

def about_us(request):
    return render(request, 'index/about_us.html')
