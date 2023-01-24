from django.db import models

class Productos(models.Model):
    CONDITION_CHOICES = (
        ('Chica', 'Chica'),
        ('Mediana','Mediana'),
        ('Grande','Grande'),
    )
    nombre = models.CharField(max_length=100)
    talla = models.CharField(max_length=50, choices = CONDITION_CHOICES)
    precio = models.FloatField()
    stock = models.BooleanField(default=True)
