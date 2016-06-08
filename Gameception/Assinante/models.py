from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# SEMPRE QUE ADICIONAR ALGUMA CLASSE AQUI, LEMBRAR DE ADICIONAR EM ADMIN.PY
# PARA PODER MANIPULAR QUALQUER DADO COMO ADM.

# coloquei aqui tambem as classes Pedido, Genero e Jogo,
# pois o historico e os dados de assinatura dependem deles.
# talvez exista um jeito melhor de organizar isso, mas veremos com o tempo

TIPOS_MIDIA = (
    ('FISICA', 'Fisica'),
    ('DIGITAL', 'Digital'),
)

class Assinante(models.Model):
    CPF = models.CharField(max_length=11)
    nome = models.CharField(max_length=200)
    usuario = models.OneToOneField(User)
    # tirei os gets e sets por motivos de: ja existem as funções do django que fazem isso
    # se em algum momento for necessario a gente poe de volta
    def __str__(self): # chave primaria que vai ser mostrada no banco de dados das assinaturas
        return self.usuario.username # pra mostrar o cpf do assinante ao inves de 'Assinante object'

class EnderecoAssinatura(models.Model):
    assinatura = models.OneToOneField(User)
    rua = models.CharField(max_length=200)
    numeroRua = models.IntegerField(default = 0)
    complemento = models.CharField(max_length=200)
    CEP = models.CharField(max_length=9)

    def __str__(self):
        return self.assinatura.username

class Genero(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class DadosAssinatura(models.Model):
    assinatura = models.OneToOneField(User)
    generosPessoais = models.ManyToManyField('Genero')
    quantidade = models.IntegerField(default=0)
    precoPorJogo = models.IntegerField(default=0)
    tipoMidia = models.CharField(max_length=10,choices=TIPOS_MIDIA,default='DIGITAL',)
    atividade = models.BooleanField(default=False)
    sistOp = models.ForeignKey('SistOp',null=True) #mostra as opcoes de sistemas operacionais pra escolher
    memRAM = models.IntegerField(default=0)
    processador = models.ForeignKey('Processadores',null=True)
    memVideo = models.IntegerField(default=0)

    def __str__(self):
        return self.assinatura.username


class Pedido(models.Model):
    historico = models.ForeignKey('HistoricoJogos')
    jogosPedidos = models.ManyToManyField('Jogo')
    codigoRastreamento = models.CharField(max_length=200)
    data = models.DateField()
    numero = models.IntegerField(default=0)
    tipoMidia = models.CharField(max_length=10,
        choices=TIPOS_MIDIA,
        default='DIGITAL',)

    def __str__(self):
        return self.historico.assinatura.username + str(self.numero)

#classe para as chaves, com a mesma ideia do sistOp ai em baixo
class Processadores(models.Model):
    proc = models.CharField(max_length=200)

    def __str__(self):
        return self.proc

class ChaveDownload(models.Model):
    jogo = models.ForeignKey('Jogo')
    pedido = models.ForeignKey('Pedido')
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
    img1 = models.CharField(max_length=200)
    img2 = models.CharField(max_length=200)
    tipoMidia = models.CharField(max_length=10,choices=TIPOS_MIDIA,default='DIGITAL',)

    def __str__(self):
            return self.nome;


class DadosBancarios(models.Model):
    assinatura = models.OneToOneField(User)
    numeroCartao = models.CharField(max_length=20)
    codigoSeguranca = models.CharField(max_length=3)
    nomeTitular = models.CharField(max_length=200)
    vencimento = models.CharField(max_length=200)

    def __str__(self):
        return self.assinatura.username

class HistoricoJogos(models.Model):
    assinatura = models.OneToOneField(User)

    def __str__(self):
        return self.assinatura.username
