import random
import datetime

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
from .models import Genero
from .models import SistOp
from .models import Processadores
from .models import ChaveDownload
from .models import HistoricoJogos
from .models import Pedido
from .models import Jogo


def MinhaConta(request): #O NOME DESSA FUNCAO DEVE SER O MESMO DO .HTML, SENAO DA ERRO. # python manage.py runserver 192.168.1.122:5555
    #endereco = EnderecoAssinatura.objects.get(id=1) #peguei um endereco de assinatura que registrei no bd, so pra teste
    if request.method == 'POST':
        assin = DadosAssinatura.objects.get(assinatura=request.user)
        assin.atividade = not assin.atividade
        assin.save()

    context_dict = {}

    try:
        infos_pagamento = DadosBancarios.objects.get(assinatura=request.user)
        context_dict['tem_infos_pagamento'] = True
        context_dict['infos_pagamento'] = infos_pagamento
    except:
        context_dict['tem_infos_pagamento'] = False

    try:
        infos_endereco = EnderecoAssinatura.objects.get(assinatura=request.user)
        context_dict['tem_infos_endereco'] = True
        context_dict['infos_endereco'] = infos_endereco
    except:
        context_dict['tem_infos_endereco'] = False

    try:
        assinatura = DadosAssinatura.objects.get(assinatura=request.user)
        context_dict['tem_assinatura'] = True
        context_dict['assinatura'] = assinatura
        context_dict['generos'] = assinatura.generosPessoais.all()
        print('a',assinatura.generosPessoais.all())
    except:
        context_dict['tem_assinatura'] = False
        context_dict['generos'] = []

    try:
        historico = HistoricoJogos.objects.get(assinatura=request.user)
        pedidos = Pedido.objects.filter(historico=historico)
        if len(pedidos) > 0:
            context_dict['tem_pedido_para_mostrar'] = True
            pedido_recente = pedidos.order_by('-numero')[0]
            context_dict['pedido_recente'] = pedido_recente
            if pedido_recente.tipoMidia == 'DIGITAL':
                context_dict['digital'] = True
                try:
                    context_dict['chaves'] = ChaveDownload.objects.filter(pedido=pedido_recente)
                except:
                    pass
            else:
                context_dict['digital'] = False
        else:
            context_dict['tem_pedido_para_mostrar'] = False
    except:
        context_dict['tem_pedido_para_mostrar'] = False

    context_dict['dados_completos'] = context_dict['tem_infos_endereco'] and context_dict['tem_infos_pagamento']



    return render(request, 'Assinante/Assinante.html', context_dict)
# esse nome no final (endereco) vai ser referenciado no .html pra mostrar os dados
# no fim, nao precisava dos gets tambem, mas deixei la por enquanto

def Historico(request):
    return render(request, 'Assinante/Historico.html', {})


##################################################

def randomString(n):
    alfa = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    ret = ""
    for i in range(n):
        ret += alfa[random.randint(0,len(alfa)-1)]
    return ret


def GerenciarEntregas(request):
    if not request.user.is_staff:
        return HttpResponseRedirect("/Assinante/")

    if request.method == 'POST':
        a = DadosAssinatura.objects.filter(atividade=True)
        for assin in a:
            #preencher campos exceto listaJogos
            userAssin = assin.assinatura
            novoPedido = Pedido()
            novoPedido.historico = HistoricoJogos.objects.get_or_create(assinatura=userAssin)[0]
            novoPedido.tipoMidia = assin.tipoMidia
            if novoPedido.tipoMidia == "FISICA":
                novoPedido.codigoRastreamento = randomString(16)
            else:
                novoPedido.codigoRastreamento = ""
            novoPedido.data = datetime.datetime.now().date()
            try:
                pedidosAssin = Pedido.objects.filter(historico=novoPedido.historico)
            except:
                pedidosAssin = None
            try:
                novoPedido.numero = len(pedidosAssin)
            except:
                novoPedido.numero = 0
            # descobrir os jogos do usuário
            jogosAssin = None
            if pedidosAssin:
                jogosAssin = pedidosAssin[0].jogosPedidos.all()
                for p in pedidosAssin:
                    jogosAssin = jogosAssin | p.jogosPedidos.all()
                print(jogosAssin)
            #descobrir os jogos disponiveis
            generosAssin = assin.generosPessoais.all()
            jogosDisp = generosAssin[0].jogo_set.all()
            for g in generosAssin:
                jogosDisp = jogosDisp | g.jogo_set.all()
            if jogosAssin:
                for jogo in jogosAssin:
                    jogosDisp = jogosDisp.exclude(pk=jogo.pk)
            jogosDisp = jogosDisp.filter(preco__lte=assin.precoPorJogo,memRAM__lte=assin.memRAM,tipoMidia=assin.tipoMidia)
            print(jogosDisp.all())
            numViavel = min(len(jogosDisp.all()),assin.quantidade)
            escolhidos = list(range(len(jogosDisp.all())))
            escolhidos = random.sample(escolhidos,numViavel)
            novoPedido.save()
            for ind in escolhidos:
                jogoAdd = jogosDisp.all()[ind]
                novoPedido.jogosPedidos.add(jogoAdd)
            novoPedido.save()
            if assin.tipoMidia == 'DIGITAL':
                for jogoAdd in novoPedido.jogosPedidos.all():
                    ChaveDownload.objects.create(jogo=jogoAdd,pedido=novoPedido,chave=randomString(10))

    context_dict = {}
    try:
        ultimaEntrega = Pedido.objects.order_by('-data')[0]
    except:
        ultimaEntrega = None
    context_dict['ultimaEntrega'] = ultimaEntrega
    context_dict['delta'] = datetime.datetime.now().date() - ultimaEntrega.data

    return render(request, 'Assinante/GerenciarEntregas.html', context_dict)

###################################################

def HistoricoPedido(request, num_pedido):

    context_dict = {}
    numPedido = int(num_pedido)
    pedido = Pedido.objects.get(historico=(HistoricoJogos.objects.get(assinatura=request.user)),numero=numPedido)
    context_dict['listaPedidos'] = Pedido.objects.filter(historico=(HistoricoJogos.objects.get(assinatura=request.user))).order_by('-data')
    print("X",context_dict['listaPedidos'])
    context_dict['pedido'] = pedido
    numPedidos = len(Pedido.objects.all())
    preco = 0
    for j in pedido.jogosPedidos.all():
        preco += j.preco
    context_dict['preco'] = preco
    if pedido.tipoMidia == 'DIGITAL':
        context_dict['chaves'] = ChaveDownload.objects.filter(pedido=pedido)
        context_dict['digital'] = True
    if numPedido > 0:
        context_dict['anterior'] = numPedido - 1
        context_dict['temAnterior'] = True
    if numPedido < numPedidos - 1:
        context_dict['proximo'] = numPedido + 1
    return render(request, 'Assinante/HistoricoPedido.html', context_dict)
'''
    var = int(num_pedido)
    num1 = int(2*var-1)
    num2 = int(2*var)
    historico = HistoricoJogos.objects.get(assinatura=request.user)
    pedidos = Pedido.objects.filter(historico=historico)
    try:
        pedido1 = Pedido.objects.get(historico=historico,numero=num1)
    except:
        pedido1 = None
    try:
        pedido2 = Pedido.objects.get(historico=historico,numero=num2)
    except:
        pedido2 = None
    print(pedido1)
    print(pedido2)
    antecessor = var - 1
    pode_antecessor = True
    sucessor = var + 1
    pode_sucessor = True
    if var >= len(pedidos) - 1:
        pode_sucessor = False
    if var <= 0:
        pode_antecessor = False
    context_dict = {'num_pedido': num_pedido, 'pedido1': pedido1, 'pedido2': pedido2}
    context_dict['antecessor'] = antecessor
    context_dict['pode_antecessor'] = pode_antecessor
    context_dict['sucessor'] = sucessor
    context_dict['pode_sucessor'] = pode_sucessor
    if pedido1 != None:
        if pedido1.tipoMidia == 'DIGITAL':
            context_dict['digital1'] = True
            try:
                context_dict['chaves1'] = ChaveDownload.objects.filter(pedido=pedido1)
            except:
                pass
        else:
            context_dict['digital1'] = False
    if pedido2 != None:
        if pedido2.tipoMidia == 'DIGITAL':
            context_dict['digital2'] = True
            try:
                context_dict['chaves2'] = ChaveDownload.objects.filter(pedido=pedido2)
            except:
                pass
        else:
            context_dict['digital2'] = False
'''


def EditarCadastro(request):
    return render(request, 'Assinante/EditarCAdastro.html', {})

def InfoPagamento(request):
    finalizado = False
    if request.method == 'POST':
        form = InfoPagamentoForm(request.POST)      #Se o request for POST o usuario esta submetendo o formulario
        if form.is_valid():
            numeroCartao = form.cleaned_data['numeroCartaoForm']        #Obtem os valores submetidos pelo usuario atraves do formulario
            codigoSeguranca = form.cleaned_data['codigoSegurancaForm']
            nomeTitular = form.cleaned_data['nomeTitularForm']
            vencimento = form.cleaned_data['vencimentoForm']
            username = request.user.get_username()                  #Obtem o nome do usuario
            user = User.objects.get(username=username)
            try:
                dados = DadosBancarios.objects.get(assinatura=user)     #Verifica se o usuario em questao ja possui dados bancarios
            except:     #Colocar o tipo do except
                dados = DadosBancarios.objects.create(assinatura=user)  #Se o usuario nao possuir dados bancarios ainda um objeto eh criado para armazena-los
            dados.numeroCartao = numeroCartao                   #Armazena os dados obtidos do formulario no objeto dados
            dados.codigoSeguranca = codigoSeguranca
            dados.nomeTitular = nomeTitular
            dados.vencimento = vencimento
            dados.save()                            #Salva as alteracoes para o banco de dados
            finalizado = True
    else:
        form = InfoPagamentoForm()
        try:
            username = request.user.get_username()
            user = User.objects.get(username=username)
            dados = DadosBancarios.objects.get(assinatura=user)         #Verifica se o usuario ja possui dados bancarios
            form.fields["numeroCartaoForm"].initial = dados.numeroCartao
            form.fields["codigoSegurancaForm"].initial = dados.codigoSeguranca     #Se existem dados bancarios antigos, estes sao mostrados ao usuario
            form.fields["nomeTitularForm"].initial = dados.nomeTitular             #permitindo a ele alterar alguns valores sem ter que reescrever os demais
            form.fields["vencimentoForm"].initial = dados.vencimento
        except:     #Colocar o tipo do except
            pass
    return render(request, 'Assinante/InfoPagamento.html', {'form': form, 'finalizado': finalizado})

def CadastroEndereco(request):
    registrado = False
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            rua = form.cleaned_data['ruaForm']
            numeroRua = form.cleaned_data['numeroRuaForm']
            complemento = form.cleaned_data['complementoForm']
            CEP = form.cleaned_data['CEPForm']
            try:
                endereco = EnderecoAssinatura.objects.get(assinatura=request.user)
            except:
                endereco = EnderecoAssinatura.objects.create(assinatura=request.user)
            endereco.rua = rua
            endereco.numeroRua = numeroRua
            endereco.complemento = complemento
            endereco.CEP = CEP
            endereco.save()
            registrado = True
    else:
        form = EnderecoForm()
        try:
            endereco = EnderecoAssinatura.objects.get(assinatura=request.user)
            form.fields['ruaForm'].initial = endereco.rua
            form.fields['numeroRuaForm'].initial = endereco.numeroRua
            form.fields['complementoForm'].initial = endereco.complemento
            form.fields['CEPForm'].initial = endereco.CEP
        except:
            pass
    return render(request, 'Assinante/CadastroEndereco.html', {'form': form, 'registrado': registrado})

def Assinatura(request):
    registrado = False
    if request.method == 'POST':
        form = DadosAssinaturaForm(request.POST)
        if form.is_valid():
            generosPessoais = form.cleaned_data['generosPessoaisForm']
            quantidade = form.cleaned_data['quantidadeForm']
            precoPorJogo = form.cleaned_data['precoPorJogoForm']
            tipoMidia = form.cleaned_data['tipoMidiaForm']
            sistOp = form.cleaned_data['sistOpForm']
            memRAM = form.cleaned_data['memRAMForm']
            processador = form.cleaned_data['processadorForm']
            memVideo = form.cleaned_data['memVideoForm']
            try:
                dados = DadosAssinatura.objects.get(assinatura=request.user)
            except:
                dados = DadosAssinatura.objects.create(assinatura=request.user)
            dados.generosPessoais = generosPessoais
            dados.quantidade = quantidade
            dados.precoPorJogo = precoPorJogo
            dados.tipoMidia = tipoMidia
            dados.sistOp = sistOp
            dados.memRAM = memRAM
            dados.processador = processador
            dados.memVideo = memVideo
            dados.atividade = True
            dados.save()
            registrado = True
    else:
        form = DadosAssinaturaForm()
        try:
            dados = DadosAssinatura.objects.get(assinatura=request.user)
            form.fields['generosPessoaisForm'].initial = dados.generosPessoais.all()
            form.fields['quantidadeForm'].initial = dados.quantidade
            form.fields['precoPorJogoForm'].initial = dados.precoPorJogo
            form.fields['tipoMidiaForm'].initial = dados.tipoMidia
            form.fields['sistOpForm'].initial = dados.sistOp
            form.fields['memRAMForm'].initial = dados.memRAM
            form.fields['processadorForm'].initial = dados.processador
            form.fields['memVideoForm'].initial = dados.memVideo
        except:
            pass
    return render(request, 'Assinante/Assinatura.html', {'form': form, 'registrado': registrado})

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

class DadosAssinaturaForm(forms.Form):
    generosPessoaisForm = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Genero.objects.all())
    quantidadeForm = forms.IntegerField(min_value=1)
    precoPorJogoForm = forms.IntegerField(min_value=1)
    tipoMidiaForm = forms.ChoiceField(widget=forms.Select(), choices=(('FISICA', 'Fisica'),('DIGITAL', 'Digital'),))
    sistOpForm = forms.ModelChoiceField(widget=forms.Select(), queryset=SistOp.objects.all())
    memRAMForm = forms.IntegerField(min_value=1)
    processadorForm = forms.ModelChoiceField(widget=forms.Select(), queryset=Processadores.objects.all())
    memVideoForm = forms.IntegerField(min_value=1)
    def __init__(self, *args, **kwargs):
        super(DadosAssinaturaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if(field != self.fields['generosPessoaisForm']):
                field.widget.attrs['class'] = 'form-control'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class AssinanteForm(forms.ModelForm):
    CPF = forms.CharField(min_length=11,max_length=11)
    class Meta:
        model = Assinante
        fields = ('CPF', 'nome')
    def __init__(self, *args, **kwargs):
        super(AssinanteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class EnderecoForm(forms.Form):
    ruaForm = forms.CharField(label='rua', max_length=200)
    numeroRuaForm = forms.IntegerField(label='numeroRua', min_value=1)
    complementoForm = forms.CharField(label='complemento', max_length=200,required=False)
    CEPForm = forms.CharField(label='CEP', min_length=8, max_length=8)
    def __init__(self, *args, **kwargs):
        super(EnderecoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class InfoPagamentoForm(forms.Form):
    numeroCartaoForm = forms.CharField(label='Numero do cartao', max_length=16, min_length=16)
    codigoSegurancaForm = forms.CharField(label='Codigo de seguranca', max_length=3, min_length=3)
    nomeTitularForm = forms.CharField(label='Nome do titular', max_length=200, min_length=2)
    vencimentoForm = forms.CharField(label='Ano de vencimento', max_length=4, min_length=4)

class ContatoAdminForm(forms.Form):
    assunto = forms.CharField(label='Assunto')
    menssagem = forms.CharField(label='Menssagem')
