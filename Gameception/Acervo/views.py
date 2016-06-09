from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Assinante.models import Jogo
from Assinante.models import Genero
# Create your views here.
def Acervo(request):
    filtrado = False
    jogos = Jogo.objects.order_by('-id')
    generos = Genero.objects.all()
    return render(request, 'Acervo/Acervo.html', {'generos' : generos, 'jogos' : jogos, 'filtrado' : filtrado})

def filtro(request, genero):
    filtrado = True
    generos = Genero.objects.all()
    gen = genero
    jogos = Jogo.objects.order_by('-id')
    #generoEscolhido = Genero.objects.get(nome=genero)
    #jogos = generoEscolhido.jogo_set.all().order_by('-id')
    return render(request, 'Acervo/Acervo.html', {'generos' : generos, 'jogos' : jogos, 'filtrado' : filtrado, 'gen' : gen})
