from django.urls import path
from . import views

urlpatterns = [
    path('cicloturista/crear/', views.crear_cicloturista, name="crear_cicloturista"),
    path('cicloturistas/',views.lista_cicloturistas, name="lista_cicloturistas"),
]
