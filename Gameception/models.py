from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# SEMPRE QUE ADICIONAR ALGUMA CLASSE AQUI, LEMBRAR DE ADICIONAR EM ADMIN.PY
# PARA PODER MANIPULAR QUALQUER DADO COMO ADM.

# coloquei aqui tambem as classes Pedido, Genero e Jogo,
# pois o historico e os dados de assinatura dependem deles.
# talvez exista um jeito melhor de organizar isso, mas veremos com o tempo

class Assinante(models.Model):
    #endAssinatura = models.OneToOneField(EnderecoAssinatura)
    #dAssinatura = models.OneToOneField(DadosAssinatura)
    #dBanco = models.OneToOneField(DadosBancarios)
    #histJogos = models.ForeignKey('HistoricoJogos')
    CPF = models.CharField(max_length=11)
    nome = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    estaLogado = False  # A ser implementado
    # tirei os gets e sets por motivos de: ja existem as funções do django que fazem isso
    # se em algum momento for necessario a gente poe de volta
    def __str__(self): # chave primaria que vai ser mostrada no banco de dados das assinaturas
        return self.CPF # pra mostrar o cpf do assinante ao inves de 'Assinante object'

class EnderecoAssinatura(models.Model):
    assinatura = models.OneToOneField(Assinante)
    rua = models.CharField(max_length=200)
    numeroRua = models.IntegerField()
    complemento = models.CharField(max_length=200)
    CEP = models.CharField(max_length=9)

    def __str__(self):
        return self.rua

class Genero(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class DadosAssinatura(models.Model):
    assinatura = models.OneToOneField(Assinante)
    generosPessoais = models.ManyToManyField('Genero')
    quantidade = models.IntegerField()
    tipoMidia = models.ForeignKey('TipoMidia')
    atividade = models.BooleanField(default=False)
    sistOp = models.ForeignKey('SistOp') #mostra as opcoes de sistemas operacionais pra escolher
    memRAM = models.IntegerField()
    processador = models.ForeignKey('Processadores')
    memVideo = models.IntegerField()

    def __str__(self):
        return str(self.pk)


class Pedido(models.Model):
    quantia = models.IntegerField()
    jogosPedidos = models.ManyToManyField('Jogo')
    codigoRastreamento = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    chaveDownload = models.ForeignKey('ChaveDownload')
    tipoMidia = models.ForeignKey('TipoMidia')

    def __str__(self):
        return str(self.pk)

class TipoMidia(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo

#classe para as chaves, com a mesma ideia do sistOp ai em baixo
class Processadores(models.Model):
    proc = models.CharField(max_length=200)

    def __str__(self):
        return self.proc

class ChaveDownload(models.Model):
    chave = models.CharField(max_length=20)

    def __str__(self):
        return self.chave

class SistOp(models.Model):
    sistOp = models.CharField(max_length=200)
# classe pra gente adicionar os SO no bd pro
# usuario escolher na hora do cadastro

    def __str__(self):
        return self.sistOp

class Jogo(models.Model):
    listaGeneros= models.ManyToManyField(Genero)
    preco = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
            return self.nome;


class DadosBancarios(models.Model):
    assinatura = models.OneToOneField(Assinante)
    numeroCartao = models.CharField(max_length=20)
    codigoSeguranca = models.IntegerField()
    nomeTitular = models.CharField(max_length=200)
    vencimento = models.CharField(max_length=200)

    def __str__(self):
        return self.numeroCartao

class HistoricoJogos(models.Model):
    assinatura = models.OneToOneField('Assinante')
    listaPedidos = models.ManyToManyField('Pedido')

    def __str__(self):
        return str(self.pk)
