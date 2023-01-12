"""Proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto_final.views import pagina_de_inicio
from Formula_1.views import crear_piloto, crear_escuderia, crear_circuito, lista_pilotos, lista_escuderias, lista_circuitos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('página-principal/', pagina_de_inicio),

    path('crear-piloto/', crear_piloto),
    path('crear-escuderia/', crear_escuderia),
    path('crear-circuito/', crear_circuito),
    path('lista-pilotos/', lista_pilotos),
    path('lista-escuderias/', lista_escuderias),
    path('lista-circuitos/', lista_circuitos),

]
