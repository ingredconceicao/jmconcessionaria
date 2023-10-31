from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, VeiculoModelForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

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

def perfil_vendedor(request):
    if str(request.method) == 'POST':
        form = VeiculoModelForm(request.POST, request.FILES)
        if form.is_valid():
            perf = form.save(commit=False)

            print(f'Marca {marca}')
            print(f'Modelo {modelo}')
            print(f'quilometragem {quilometragem}' )
            print(f'valor {valor}' )
            print(f'ano {ano}' )
            print(f'estoque {estoque}')
            print(f'condicao {condicao}' )
            print(f'imagem {imagem}')

            messages.success(request, 'Veiculo cadastrado com Sucesso!')

        else:
            messages.error(request, 'veiculo Não cadastrado.') 

        context = {
            'form': form
        }       
        return render(request, 'perfil_vendedor.html', context)

