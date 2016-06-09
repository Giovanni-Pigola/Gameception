from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Assinante.models import Jogo
from Assinante.models import Genero
# Create your views here.
def Acervo(request):
    jogos = Jogo.objects.order_by('-id')
    generos = Genero.objects.all()
    filtrado = False #indica se foi clicado em algum dos generos pra filtrar
    return render(request, 'Acervo/Acervo.html', {'generos' : generos, 'jogos' : jogos, 'filtrado' : filtrado})

def filtro(request, genero):
    filtrado = True
    gen = "RPG" #coloquei como rpg pra teste. ele filtra certinho. mas pelo visto, ele nao ta pegando o 'genero' ainda na funcao
    #se poe gen = str(genero), ele pega '' (vi isso quando tava dando outros erros na hora de implementar o filtro)
    #arrumado esse detalhe, o fltro funciona
    generos = Genero.objects.all()
    jogos = Jogo.objects.order_by('-id')
    return render(request, 'Acervo/Acervo.html', {'generos' : generos, 'jogos' : jogos, 'gen' : gen , 'filtrado' : filtrado})
