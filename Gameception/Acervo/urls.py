from django.conf.urls import include, url
from Assinante.models import Genero
from . import views

urlpatterns = [
    url(r'^$', views.Acervo, name = "Acervo"),
    #url(r'^/AcervoFiltro/', views.filtro, name="AcervoFiltro"),
    url(r'^/(?P<genero>[-\w ]+)/', views.filtro, name="AcervoFiltro"),
]
