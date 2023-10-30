from typing import Any
from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):

    nome = forms.CharField(label='nome', max_length=100)
    telefone = forms.CharField(label='telefone', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    assunto = forms.CharField(label='assunto', max_length=100)
    descricao = forms.CharField(label='descricao', widget=forms.Textarea())

    # def enviar_email(self):
    #     nome = self.cleaned_data['nome']
    #     email = self.cleaned_data['email']
    #     assunto = self.cleaned_data['assunto']
    #     descricao = self.cleaned_data['descricao']

    #     conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\n Descrição: {descricao}'

    #     mail = EmailMessage(
    #         subject='E-mail enviado com sucesso.',
    #         body=conteudo,
    #         from_email='contato@seudominio.com.br',
    #         to=['contato@seudominio.com.br',],
    #         headers={'Reply-To': email}  

    #     )
    #     mail.send()