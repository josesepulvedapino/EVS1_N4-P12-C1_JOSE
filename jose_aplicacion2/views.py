from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def v1p2(request):
    return HttpResponse("<h1>Vista 1, Aplicacion 2</h1>")
def v2p2(request):
    return HttpResponse("<h1>Vista 2, Aplicacion 2</h1>")
