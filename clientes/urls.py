from django.urls import path
from . import views

urlpatterns = [
    path('cicloturista/crear/', views.crear_cicloturista, name="crear_cicloturista"),
    path('cicloturistas/',views.lista_cicloturistas, name="lista_cicloturistas"),
    path('corredor/crear/', views.crear_corredor, name="crear_corredor"),
    path('corredores/',views.lista_corredores, name="lista_corredores"),
    path('ruta/crear/',views.crear_ruta, name="crear_ruta"),    
]