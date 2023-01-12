from django.contrib import admin

from Formula_1.models import Pilotos, Escuderias, Circuitos

@admin.register(Pilotos)
class PilotosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'nacionalidad')


@admin.register(Escuderias)
class EscuderiasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'sede', 'año_de_fundacion')

@admin.register(Circuitos)
class CircuitosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'longitud', 'capacidad')

# Register your models here.
