from django import forms


class CadastroForm (forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    usuario = forms.CharField(label='Nome', max_length=100)
    senha = forms.CharField(label='Nome', max_length=100)
    senha2 = forms.CharField(label='Nome', max_length=100)