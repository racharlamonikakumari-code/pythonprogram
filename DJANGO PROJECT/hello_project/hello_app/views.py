from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django Project!")

def show(request):
    return HttpResponse("Monika")
