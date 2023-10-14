from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def carros(request):
    return render(request, 'carros.html')

def contato(request):
    return render(request, 'contato.html')