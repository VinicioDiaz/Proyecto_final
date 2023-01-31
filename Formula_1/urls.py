from django.urls import path
from Formula_1.views import crear_piloto, crear_escuderia, crear_circuito, lista_pilotos, lista_escuderias, lista_circuitos, Posicion_mundial_piloto, Posicion_mundial_constructor

urlpatterns = [ 
    path('crear-piloto/', crear_piloto),
    path('crear-escuderia/', crear_escuderia), 
    path('crear-circuito/', crear_circuito),
    path('lista-pilotos/', lista_pilotos),
    path('lista-escuderias/', lista_escuderias),
    path('lista-circuitos/', lista_circuitos),
    path('clasificacion-pilotos/', Posicion_mundial_piloto),
    path('clasificacion-constructores/', Posicion_mundial_constructor),
]