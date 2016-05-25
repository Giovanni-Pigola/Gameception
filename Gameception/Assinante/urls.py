from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.Assinante, name="Assinante"), #joga para a função Assinante em views.py
]
