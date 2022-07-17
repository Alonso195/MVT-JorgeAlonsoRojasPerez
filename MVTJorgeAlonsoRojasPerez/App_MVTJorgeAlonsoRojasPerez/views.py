from django.http import HttpResponse
from django.shortcuts import render

from App_MVTJorgeAlonsoRojasPerez.models import Familiares


def inicio(self):
    return render(self, "inicio.html")

def familiar(self, nombre, apellidos, parentesco, nacimiento, edad):

    familiar = Familiares(nombre=nombre, apellidos=apellidos,
    parentesco=parentesco, nacimiento=nacimiento, edad=edad)
    familiar.save()

    return HttpResponse(f"""
        <p>Familiar {familiar.nombre} {familiar.apellidos} creado con exito!!</p> 
    """)

def lista_familiares(self):
    lista = Familiares.objects.all()
    return render(self, "lista_familiares.html", {"lista_familiares":lista})
