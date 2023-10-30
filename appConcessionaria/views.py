from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def carros(request):
    return render(request, 'carros.html')

def contato(request):

    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST' :
        form.is_valid()  
        if form.errors:  
            messages.error(request, 'Operação falhou. Corrija os erros no formulário.')
        else:
            form.send_mail()  
            messages.success(request, 'Operação efetuada com sucesso.')
            form = ContatoForm()

    context = {
        'form':form
    }
    return render(request, 'contato.html', context)

def login(request):
    return render(request, 'login.html')

def cadastro(request):
     
    return render(request, 'cadastro.html')
