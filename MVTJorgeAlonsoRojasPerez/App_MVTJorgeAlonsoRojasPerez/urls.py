from django.urls import path
from App_MVTJorgeAlonsoRojasPerez.views import inicio, lista_familiares, familiar

urlpatterns = [    
    path('', inicio),
    path('agrega-familiar/<nombre>/<apellidos>/<parentesco>/<nacimiento>/<edad>', familiar),
    path('lista-familiares/', lista_familiares),
]
