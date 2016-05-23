from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms

def MainPage(request):
    return render (request, 'MainPage.html', {})
