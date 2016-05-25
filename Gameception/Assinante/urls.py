from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.MinhaConta, name="MinhaConta"), #joga para a função Assinante em views.py
]
