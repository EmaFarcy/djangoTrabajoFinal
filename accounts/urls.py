from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import mi_login, registrarse, editar_usuario

urlpatterns = [
    path('login/', mi_login, name='login'),
    path('editar/', editar_usuario, name='editar_usuario'),
    path('registrarse/', registrarse, name='registrarse'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout')   
]


   