from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^', views.index, name = home),
    url(r'^Home/', views.index, name = home),
    url(r'^Sobre/', views.Sobre, name = Sobre),
    url(r'^Contatos/', views.Contatos, name = Contatos)
]