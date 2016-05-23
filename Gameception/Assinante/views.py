from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from .models import Assinante
from .models import EnderecoAssinatura
from .models import DadosAssinatura
from .models import DadosBancarios


def Assinante(request): #O NOME DESSA FUNCAO DEVE SER O MESMO DO .HTML, SENAO DA ERRO.
    endereco = EnderecoAssinatura.objects.get(id=1) #peguei um endereco de assinatura que registrei no bd, so pra teste
    return render (request, 'Assinante.html', {'endereco' : endereco})
# esse nome no final (endereco) vai ser referenciado no .html pra mostrar os dados
# no fim, nao precisava dos gets tambem, mas deixei la por enquanto


class AssinanteForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100, min_length=4)
