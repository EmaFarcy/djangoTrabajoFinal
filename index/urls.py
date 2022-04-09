from django.urls import path
from .views import index, nosotros, about_us, bike_shop

urlpatterns = [
    path('', index, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('about_us/', about_us, name='about_us'),
    path('bike_shop/', bike_shop, name='bike_shop')
]