from django.contrib import admin
from Tienda.models import Productos

@admin.register(Productos)
class PlayeraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'talla', 'precio', 'stock')
