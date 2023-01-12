from django.contrib import admin

from Formula_1.models import Pilotos, Escuderias, Circuitos, Posicion_pilotos_2022, Posicion_constructores_2022

@admin.register(Pilotos)
class PilotosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'nacionalidad')


@admin.register(Escuderias)
class EscuderiasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'sede', 'año_de_fundacion')

@admin.register(Circuitos)
class CircuitosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'longitud', 'capacidad')

@admin.register(Posicion_pilotos_2022)
class Posicion_pilotos_2022Admin(admin.ModelAdmin):
    list_display = ('posicion', 'conductor', 'nacionalidad', 'auto', 'puntos') 

@admin.register(Posicion_constructores_2022)
class Posicion_constructores_2022Admin(admin.ModelAdmin):
    list_display = ('posicion', 'equipo', 'puntos') 


# Register your models here.
