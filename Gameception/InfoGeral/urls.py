from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^', views.index, {}),
    url(r'^Home/', views.index, {}),
    url(r'^Sobre/', views.Sobre, {}),
    url(r'^Contatos/', views.Contatos, {})
]