from django.urls import path
from.views import home, contato, carros

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('carros/', carros, name='carros'),
]