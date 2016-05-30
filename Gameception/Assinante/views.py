from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User

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
    return render(request, 'MainPage2.html', {})

def HistoricoPedido(request, num_pedido):
    return render(request, 'Assinante/HistoricoPedido.html', {'num_pedido' : num_pedido, })

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

def Cadastro(request):
    registrado = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        assinante_form = AssinanteForm(data=request.POST)
        if user_form.is_valid() and assinante_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            assinante = assinante_form.save(commit=False)
            assinante.usuario = user
            assinante.save()
            print(assinante.usuario)
            registrado = True
        else:
            print (user_form.errors, assinante_form.errors)
    else:
        user_form = UserForm()
        assinante_form = AssinanteForm()
    return render(request,
            'Assinante/Cadastro.html',
            {'user_form': user_form, 'registrado': registrado, 'assinante_form' : assinante_form} )

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/Assinante/')
            else:
                return HttpResponse(" account is disabled.")
        else:
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'Assinante/Login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AssinanteForm(forms.ModelForm):
    class Meta:
        model = Assinante
        fields = ('CPF', 'nome')

class InfoPagamentoForm(forms.Form):
    numeroCartaoForm = forms.CharField(label='Numero do cartao', max_length=16, min_length=16)
    codigoSegurancaForm = forms.CharField(label='Codigo de seguranca', max_length=3, min_length=3)
    nomeTitularForm = forms.CharField(label='Nome do titular', max_length=200, min_length=2)
    vencimentoForm = forms.CharField(label='Ano de vencimento', max_length=4, min_length=4)
