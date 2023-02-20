from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    return HttpResponse("hola Django -Hola como estas")

def saludar_a(request, nombre, apellido=''):
    return HttpResponse(f"Hola como estas {nombre.capitalize()} {apellido.capitalize()}")
