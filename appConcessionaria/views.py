from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, VeiculoModelForm
from .models import Veiculo
# Create your views here.

def home(request):
    context = {
        'veiculos': Veiculo.objects.all()
    }
    return render(request, 'home.html', context)

def carros(request):
    return render(request, 'carros.html')

def contato(request):

    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST' :
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            descricao = form.cleaned_data['descricao']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'Nome: {email}')
            print(f'Nome: {assunto}')
            print(f'Nome: {descricao}')

            messages.success(request='Email enviado com sucesso!')
            form = ContatoForm()
        else: 
            messages.error(request,'Erro ao enviar o E-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def login(request):
    return render(request, 'login.html')

def cadastro(request):
     
    return render(request, 'cadastro.html')

def perfil(request):
    if str(request.method) == 'POST':
        form = VeiculoModelForm(request.POST, request.FILES)
        print('a')
        print(form.errors.as_json())

        if form.is_valid():
            print('b')
            form.save()
            messages.success(request, 'Veiculo cadastrado com Sucesso!')
            form = VeiculoModelForm()


        else:
            messages.error(request, 'veiculo Não cadastrado.') 
    else:
        form = VeiculoModelForm()
    context = {
        'form': form
    }       
    return render(request, 'perfil_vendedor.html', context)

def loginVendedor(request):
     
    return render(request, 'login_f.html')
