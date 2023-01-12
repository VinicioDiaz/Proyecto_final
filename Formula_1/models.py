from django.db import models

class Pilotos(models.Model):
    nombre = models.CharField(max_length=70)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=30)

class Escuderias(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=30)
    sede = models.CharField(max_length=50)
    año_de_fundacion = models.IntegerField()

class Circuitos(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    longitud = models.CharField(max_length=20)
    capacidad = models.CharField(max_length=35)
