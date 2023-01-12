from django.urls import path
from Formula_1.views import pagina_de_inicio, crear_piloto, crear_escuderia, crear_circuito, lista_pilotos, lista_escuderias, lista_circuitos

urlpatterns = [ 
    path('página-principal/', pagina_de_inicio),
    path('crear-piloto/', crear_piloto),
    path('crear-escuderia/', crear_escuderia), 
    path('crear-circuito/', crear_circuito),
    path('lista-pilotos/', lista_pilotos),
    path('lista-escuderias/', lista_escuderias),
    path('lista-circuitos/', lista_circuitos),
]