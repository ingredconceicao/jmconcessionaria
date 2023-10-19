from django.shortcuts import render
from .forms import CadastroForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def carros(request):
    return render(request, 'carros.html')

def contato(request):
    return render(request, 'contato.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    form = CadastroForm()
    context = {
        'form': form
        }
    
    return render(request, 'cadastro.html', context)