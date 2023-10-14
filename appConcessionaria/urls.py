from django.urls import path
from .views import home, carros, contato

urlpatterns = [ 
    path('', home, name='home'),
    path('carros/', carros, name='carros'),
    path('contato', contato, name='contato'),
    ]