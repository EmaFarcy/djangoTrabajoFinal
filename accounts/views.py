from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import AeroUserForm, EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension 

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
                return render(request, 'accounts/login.html', {'login_form': login_form, 'msj': msj})
        
        else:
            msj= 'Warning! El formulario no es válido.'
            return render(request, 'accounts/login.html', {'login_form': login_form, 'msj': msj})
            
    login_form= AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form': login_form, 'msj': msj})

def registrarse(request):
    
    if request.method== 'POST':
        form= AeroUserForm(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/registrarse.html', {'form': form, 'msj': 'El formulario no es válido'})
            
    registro_form= AeroUserForm()
    return render(request, 'accounts/registrarse.html', {'registro_form': registro_form})

@login_required
def editar_usuario(request):
    
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    if request.method== 'POST':
        form= EditFullUser(request.POST, request.FILES)  
        if form.is_valid():
            
            data = form.cleaned_data
            request.user.email = data.get('email',)
            request.user.first_name = data.get('first_name')
            request.user.last_name = data.get('last_name', '')      
            
            avatar = data.get('avatar', '')
            if avatar is not None:
                if avatar is False:
                    user_extension_logued.avatar = None
                else:
                    user_extension_logued.avatar = data.get('avatar')
            user_extension_logued.link = data.get('link', '')
            user_extension_logued.more_description = data.get('more_description','')
                
                
               
            #    request.user.email = form.cleaned_data['email']
            #    request.user.first_name = form.cleaned_data['first_name']
            #    request.user.last_name = form.cleaned_data['last_name']
            #    user_extension_logued.avatar= form.cleaned_data['avatar']
            #    user_extension_logued.link = form.cleaned_data['link']
            #    user_extension_logued.more_description = form.cleaned_data['more_description']
               
            if form.cleaned_data['password1'] != '' and form.cleaned_data ['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
           
            request.user.save()
            user_extension_logued.save()
               
            return redirect('index')
        else:
            return render(request, 'accounts/editar_usuario.html', {'form': form, 'msj': 'El formulario no es válido'})
            
    form= EditFullUser(
        initial={
            'email': request.user.email,  
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'more_description': user_extension_logued.more_description
    })
    return render(request, 'accounts/editar_usuario.html', {'form': form})

@login_required
def usuario_datos(request):
    return render(request, 'accounts/usuario_datos.html', {})
