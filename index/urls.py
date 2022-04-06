from django.urls import path
from .views import index, nosotros, about_us

urlpatterns = [
    path('', index, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('about_us/', about_us, name='about_us')
]