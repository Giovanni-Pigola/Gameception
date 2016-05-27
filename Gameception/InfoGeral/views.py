from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'Infos/Home.html', {})

def Sobre(request):
    return render (request, 'Infos/Sobre.html', {})

def Contatos(request):
    return render (request, 'Infos/Contatos.html', {})