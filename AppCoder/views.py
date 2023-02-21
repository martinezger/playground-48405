from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Tarea


def saludar(request):
    return HttpResponse("hola Django -Hola como estas")


def saludar_a(request, nombre, apellido=''):
    return HttpResponse(f"Hola como estas {nombre.capitalize()} {apellido.capitalize()}")


def mostrar_mis_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "AppCoder/index.html", {"tareas": tareas})

def agregar_una_tarea(request):
    nombre_tarea = request.GET.get("nombre")
    nueva_tarea = Tarea(nombre=nombre_tarea)
    nueva_tarea.save()
    return redirect('mis-tareas')

def terminar_una_tarea(request, id):
    tarea = Tarea.objects.filter(id=id).first()
    tarea.terminar()
    tarea.save()
    return redirect("mis-tareas")

def borrar_una_tarea(request, id):
    tarea = Tarea.objects.filter(id=id).first()
    tarea.delete()
    return redirect("mis-tareas")

    