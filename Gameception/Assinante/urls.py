from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^InfoPagamento/', views.InfoPagamento, name="InfoPagamento"),
    url(r'^Historico/', views.Historico, name="Historico"),
    url(r'^Cadastro/', views.Cadastro, name="Cadastro"),
    url(r'^Assinatura/', views.Assinatura, name="Assinatura"),
    url(r'^ContatoAdmin/', views.ContatoAdmin, name="ContatoAdmin"),
    url(r'^Logout/', views.user_logout, name="Logout"),
    url(r'^Login/', views.user_login, name="Login"),
    url(r'^$', views.MinhaConta, name="MinhaConta"), #joga para a função Assinante em views.py
]
