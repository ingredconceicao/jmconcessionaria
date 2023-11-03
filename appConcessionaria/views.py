from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, VeiculoModelForm, LoginUsuarioForm ,User_rigister, LoginVendedorForm
from .models import Veiculo
from django.contrib.auth import login,authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User





# Create your views here.

def home(request):
    context = {
        'veiculos': Veiculo.objects.all()
    }

    return render(request, 'home.html', context)

def carros(request):
    return render(request, 'carros.html')

def inserirVeiculo(request):
    return render(request, 'perfil_vendedor.html')

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

def login_page(request):
    if str(request.method) == 'POST':
        cpf = request.POST.get('cpf')
        print('adasd')

        password = request.POST.get('password')
        if not cpf or not password:
            print('adasd')
            return render(request, 'login.html')

        usuario = authenticate(
            request, username=cpf, password=password)
        if not usuario:
            print('adasd')
            return render(request, 'login.html')

        login(request, user=usuario)
        print('adasd')
        return render(request, 'home.html')


    
    return render(request, 'login.html')
    

def cadastro(request):
    form = User_rigister(request.POST)
    if form.is_valid():
        senha = request.POST.get('senha')
        save_usuario = form.save(commit=False)
        save_usuario.set_password(senha)
        save_usuario.save()
        form.save()
        return redirect('login')
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
   
    if request.method == 'POST':
        form = LoginVendedorForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            password = form.cleaned_data['password']
            user = authenticate(request, cpf=cpf, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil_vendedor.html')  # Redirecione para a página após o login
    else:
        form = LoginVendedorForm()

    return render(request, 'login.html', {'form': form})

    

