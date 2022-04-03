from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import AeroUserForm

def index(request):
    return render(request, 'index/index.html')

def nosotros(request):
    return render(request, 'index/nosotros.html')

def mi_login(request):
    msj= ''
    if request.method== "POST":
        login_form= AuthenticationForm(request, data=request.POST)
        
        if login_form.is_valid():
            username= login_form.cleaned_data['username']
            password= login_form.cleaned_data['password']
            user= authenticate(username=username, password= password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            
            else:
                msj= 'Error! El usuario no se pudo autenticar. El formulario reconoce mayúsculas.'
        
        else:
            msj= 'Warning! El formulario no es válido.'
            
    login_form= AuthenticationForm()
    return render(request, 'index/login.html', {'login_form': login_form, 'msj': msj})

def registrarse(request):
    
    if request.method== 'POST':
        form= AeroUserForm(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return redirect('login')
        else:
            return render(request, 'index/registrarse.html', {'form': form, 'msj': 'El formulario no es válido'})
            
        
        
    form= AeroUserForm()
    return render(request, 'index/registrarse.html', {'form': form})
