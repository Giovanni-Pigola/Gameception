from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = "Home"),                #acesso inicial da url e pelo botão home
    url(r'^Sobre', views.Sobre, name = "Sobre"),           #acesso a pagina de Sobre
    url(r'^Contatos', views.Contatos, name = "Contatos")   #acesso a pagina de Contatos
]