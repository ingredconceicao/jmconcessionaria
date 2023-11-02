from django.urls import path
from.views import home, contato, carros, login, cadastro, perfil, loginVendedor


urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('carros/', carros, name='carros'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('vendedor/', loginVendedor, name='loginVendedor'),
]