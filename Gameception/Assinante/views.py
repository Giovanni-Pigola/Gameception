from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from .models import Assinante
from .models import EnderecoAssinatura
from .models import DadosAssinatura
from .models import DadosBancarios


def MinhaConta(request): #O NOME DESSA FUNCAO DEVE SER O MESMO DO .HTML, SENAO DA ERRO.
    endereco = EnderecoAssinatura.objects.get(id=1) #peguei um endereco de assinatura que registrei no bd, so pra teste
    return render (request, 'Assinante/Assinante.html', {'endereco' : endereco})
# esse nome no final (endereco) vai ser referenciado no .html pra mostrar os dados
# no fim, nao precisava dos gets tambem, mas deixei la por enquanto

def Historico(request):
    return render(request, 'Assinante/Historico.html', {})

def Cadastro(request):
    return render(request, 'Assinante/Cadastro.html', {})

def Assinatura(request):
    return render(request, 'Assinante/Assinatura.html', {})

def InfoPagamento(request):
    if request.method == 'POST':
        form = InfoPagamentoForm(request.POST)
        if form.is_valid():
            numeroCartao = form.cleaned_data['numeroCartaoForm']
            codigoSeguranca = form.cleaned_data['codigoSegurancaForm']
            nomeTitular = form.cleaned_data['nomeTitularForm']
            vencimento = form.cleaned_data['vencimentoForm']
            #Agora precisa salvar os valores acima no banco de dados
    else:
        form = InfoPagamentoForm()
        try:
            form.fields["numeroCartaoForm"].initial = DadosBancarios.numeroCartao           #Ver isso direito
            form.fields["codigoSegurancaForm"].initial = DadosBancarios.codigoSeguranca     #Ver isso direito
            form.fields["nomeTitularForm"].initial = DadosBancarios.nomeTitular             #Ver isso direito
            form.fields["vencimentoForm"].initial = DadosBancarios.vencimento               #Ver isso direito
        except:     #Colocar o tipo do except
            pass
    return render(request, 'Assinante/InfoPagamento.html', {'form': form})

def ContatoAdmin(request):
    return render(request, 'Assinante/ContatoAdmin.html', {})


class MinhaContaForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100, min_length=4)

class InfoPagamentoForm(forms.Form):
    numeroCartaoForm = forms.CharField(label='Numero do cartao', max_length=16, min_length=16)
    codigoSegurancaForm = forms.CharField(label='Codigo de seguranca', max_length=3, min_length=3)
    nomeTitularForm = forms.CharField(label='Nome do titular', max_length=200, min_length=2)
    vencimentoForm = forms.CharField(label='Ano de vencimento', max_length=4, min_length=4)