from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms

def MainPage(request):
    return HttpResponse("Bem vindo a pagina principal.")
