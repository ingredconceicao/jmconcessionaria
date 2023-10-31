from django.urls import path
from.views import home, contato, carros, login, cadastro, perfil_vendedor

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('carros/', carros, name='carros'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil_vendedor, name='perfil_vendedor'),
]