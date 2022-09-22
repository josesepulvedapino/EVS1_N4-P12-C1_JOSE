from django.shortcuts import render
from django.http import HttpResponse

def v1p1(request):
    return HttpResponse("<h1>Vista 1, Aplicacion 1</h1>")
def v2p1(request):
    return HttpResponse("<h1>Vista 2, Aplicacion 1</h1>")