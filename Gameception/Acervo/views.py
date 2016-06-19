from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Assinante.models import Jogo
from Assinante.models import Genero
import math

def Acervo(request):
    filtrado = False
    jogos = Jogo.objects.order_by('-id')
    generos = Genero.objects.all()
    return render(request, 'Acervo/Acervo.html', {'generos' : generos, 'jogos' : jogos, 'filtrado' : filtrado})

def filtro(request, genero, pagina):
    pagina = int(pagina)
    if(genero == 'Todos'):
        listajogos = Jogo.objects.order_by('-id')
        jogos = []
        for i in range(99*(pagina-1), 99*pagina):
            try:
                jogos.append(listajogos[i])
            except:
                pass
    else:
        listajogos = Jogo.objects.filter(listaGeneros__nome=genero).order_by('-id')
        jogos = []
        for i in range(99*(pagina-1), 99*pagina):
            try:
                jogos.append(listajogos[i])
            except:
                pass
    paginas = math.ceil(len(listajogos)/99)
    listapaginas = []
    for i in range(1, paginas+1):
        listapaginas.append(i)
    generos = Genero.objects.all()
    return render(request, 'Acervo/Acervo.html', {'generos' : generos, 'jogos' : jogos, 'listapaginas': listapaginas, 'antpagina': (pagina-1), 'proxpagina': (pagina+1), 'genero': genero, 'pagina': pagina})
