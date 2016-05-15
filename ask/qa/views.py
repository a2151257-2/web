from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def nf(request, *args, **kwargs):
    return HttpResponseNotFound('Not found')
