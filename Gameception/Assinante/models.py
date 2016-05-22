from django.db import models

class Assinante(models.Model):
    CPF = models.IntegerField()
    nome = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    rua = models.CharField(max_length=200)
    numeroRua = models.IntegerField()
    complemento = models.CharField(max_length=200)
    CEP = models.IntegerField()

    estaLogado = False  # A ser implementado
