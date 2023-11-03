from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, VeiculoModelForm, CadastroUsuarioForm, LoginUsuarioForm ,User_rigister
from .models import Veiculo
from django.contrib.auth import login
from django.contrib.auth.models import User


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
    form = CadastroUsuarioForm(request.POST)
    if form.is_valid():
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        save_usuario = User_rigister
        save_usuario.set_password(senha) 
        save_usuario.username = cpf
        save_usuario.first_name = nome
        save_usuario.save()
        form.save()

    return render(request, 'cadastro.html')
    

def perfil(request):
    if str(request.method) == 'POST':
        form = VeiculoModelForm(request.POST, request.FILES)
        # print('a')
        # print(form.errors.as_json())

        if form.is_valid():
           
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

