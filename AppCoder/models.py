from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100,default="por_hacer")
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)

    def terminar(self):
        self.estado = "terminado"


    def __str__(self):
        return self.nombre



