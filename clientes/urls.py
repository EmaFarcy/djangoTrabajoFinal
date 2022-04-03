from django.urls import path
from . import views

urlpatterns = [
    path('cicloturista/crear/', views.crear_cicloturista, name="crear_cicloturista"),
    path('cicloturistas/',views.lista_cicloturistas, name="lista_cicloturistas"),
    path('cicloturistas/<int:pk>',views.DetalleCicloturista.as_view(), name="detalle_cicloturista"),
    path('cicloturistas/<int:pk>/editar',views.EditarCicloturista.as_view(), name="editar_cicloturista"),
    path('cicloturistas/<int:pk>/borrar',views.BorrarCicloturista.as_view(), name="borrar_cicloturista"),     
    path('corredor/crear/', views.crear_corredor, name="crear_corredor"),
    path('corredores/',views.lista_corredores, name="lista_corredores"),
    path('corredores/<int:pk>',views.DetalleCorredor.as_view(), name="detalle_corredor"),
    path('corredores/<int:pk>/editar',views.EditarCorredor.as_view(), name="editar_corredor"),
    path('corredores/<int:pk>/borrar',views.BorrarCorredor.as_view(), name="borrar_corredor"),
    
    
    
    path('ruta/crear/',views.crear_ruta, name="crear_ruta")
]