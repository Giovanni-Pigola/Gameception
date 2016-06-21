from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^InfoPagamento/', views.InfoPagamento, name="InfoPagamento"),
    url(r'^Endereco/', views.CadastroEndereco, name="CadastroEndereco"),
    url(r'^Historico/$', views.Historico, name="Historico"),
    url(r'^Historico/(?P<num_pedido>\d+)/', views.HistoricoPedido, name="HistoricoPedido"), #pra ver um pedido individualmente colocando o num dele na url
    url(r'^Cadastro/', views.Cadastro, name="Cadastro"),
    url(r'^Assinatura/', views.Assinatura, name="Assinatura"),
    url(r'^ContatoAdmin/', views.ContatoAdmin, name="ContatoAdmin"),
    url(r'^EditarCadastro/', views.EditarCadastro, name="EditarCadastro"),
    url(r'^EditarSenha/', views.EditarSenha, name="EditarSenha"),
    url(r'^Logout/', views.user_logout, name="Logout"),
    url(r'^Login/', views.user_login, name="Login"),
    url(r'^$', views.MinhaConta, name="MinhaConta"), #joga para a função Assinante em views.py
    url(r'^Gerenciar-Entregas/', views.GerenciarEntregas, name="GerenciarEntregas"),
    url(r'^CancelarCadastro/', views.CancelarCadastro, name="CancelarCadastro"),
    url(r'^RedefinirSenha/', views.RedefinirSenha, name="RedefinirSenha"),
]
