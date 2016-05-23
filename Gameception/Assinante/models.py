from django.db import models
from django.utils import timezone
# SEMPRE QUE ADICIONAR ALGUMA CLASSE AQUI, LEMBRAR DE ADICIONAR EM ADMIN.PY
# PARA PODER MANIPULAR QUALQUER DADO COMO ADM.

# coloquei aqui tambem as classes Pedido, Genero e Jogo,
# pois o historico e os dados de assinatura dependem deles.
# talvez exista um jeito melhor de organizar isso, mas veremos com o tempo

class Assinante(models.Model):
    CPF = models.CharField(max_length=14)
    nome = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    estaLogado = False  # A ser implementado
    # gets e sets (suspeito que nao sejam necessarios, por causa das funções .get e .update
    # que ja existem, mas vou deixar as que eu fiz ai mesmo assim)
    def __str__(self): # chave primaria que vai ser mostrada no banco de dados das assinaturas
        return self.CPF

    def getCPF(self):
        return self.CPF

    def getNome(self):
        return self.nome

    def getUsuario(self):
        return self.usuario

    def getSenha(self):
        return self.senha

    def getEmail(self):
        return self.email

    def getEstaLogado(self):
        return self.estaLogado



class EnderecoAssinatura(models.Model):
    rua = models.CharField(max_length=200)
    numeroRua = models.IntegerField()
    complemento = models.CharField(max_length=200)
    CEP = models.CharField(max_length=9)

    def getRua(self):
        return self.rua

    def getNumeroRua(self):
        return self.numeroRua

    def getComplemento(self):
        return self.complemento

    def __str__(self):
        return self.CEP

    def getCEP(self): #como eu nao sei se pode chamar a função __str__ quando for mostrar
                      # o cep na pagina, deixei as duas funções
        return self.CEP

class Genero(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def getNome(self):
        return nome

    def getDescricao(self):
        return self.descricao

class DadosAssinatura(models.Model):
    generosPessoais = models.ForeignKey('Genero')
    quantidade = models.IntegerField()
    #tipoMidia =
    atividade = models.BooleanField(default=False)
    #sistOp
    memRAM = models.IntegerField()
    #processador =
    memVideo = models.IntegerField()

#class Pedido(models.Model):
#    quantia =
#    jogosPedidos
#    codigoRastreamento
#    numeroPedido
#    data =
#    chaveDownload =
#    tipoMidia =

#class Jogo():




class DadosBancarios(models.Model):
    numeroCartao = models.CharField(max_length=20)
    codigoSeguranca = models.IntegerField()
    nomeTitular = models.CharField(max_length=200)
    vencimento = models.CharField(max_length=200)

#class HistoricoJogos(models.Model):
    # listaPedidos = models.ForeignKey('Pedido')

    #def getListaPedidos(self):
    #    return self.listaPedidos
