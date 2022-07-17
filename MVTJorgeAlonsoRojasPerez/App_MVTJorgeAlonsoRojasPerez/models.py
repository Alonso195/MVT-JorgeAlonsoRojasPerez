from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    parentesco = models.CharField(max_length=100)
    nacimiento = models.DateField()
    edad = models.IntegerField()



