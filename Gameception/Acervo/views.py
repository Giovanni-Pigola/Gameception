from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Assinante.models import Jogo
from Assinante.models import Genero
# Create your views here.
def Acervo(request):
    nomeFiltro = None
    jogos = Jogo.objects.order_by('-id')
    generos = Genero.objects.all()
    return render(request, 'Acervo/Acervo.html', {'generos' : generos, 'jogos' : jogos, 'nomeFiltro' : nomeFiltro})

def filtro(request, genero):
    nomeFiltro = "Jogos de " + genero
    generos = Genero.objects.all()
    generoEscolhido = Genero.objects.get(nome=genero)
    jogos = generoEscolhido.jogo_set.all().order_by('-id')
    return render(request, 'Acervo/Acervo.html', {'generos' : generos, 'jogos' : jogos, 'nomeFiltro' : nomeFiltro})
