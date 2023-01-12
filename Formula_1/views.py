from django.shortcuts import render
from django.http import HttpResponse

from Formula_1.models import Pilotos, Escuderias, Circuitos


def pagina_de_inicio(request):
    return render(request, 'pagina_inicio.html', context={})

def crear_piloto(request):
    nuevo_piloto = Pilotos.objects.create(nombre = 'Carlos Sainz Jr', edad = 28, nacionalidad = 'Español')  
    
    return HttpResponse('Haz creado un nuevo piloto')

def crear_escuderia(request):
    nueva_escuderia = Escuderias.objects.create(nombre = 'Oracle Red Bull Racing', nacionalidad = 'Inglesa' , sede = 'Milton Keynes, England, UK' , año_de_fundacion = 2005)
    return HttpResponse("Haz creado una nueva escunderia")

def crear_circuito(request):
    nuevo_circuito = Circuitos.objects.create(nombre = 'Circuito de Barcelona-Cataluña', ubicacion = 'Cataluña, España' , longitud = '4,675 km' , capacidad = '140,700 espectadores')
    return HttpResponse("Haz creado un nuevo circuito")







def lista_pilotos(request):
    todos_los_pilotos = Pilotos.objects.all()
    context = {
        'pilotos': todos_los_pilotos,
        }
    return render(request, 'pagina_pilotos.html', context = context)

def lista_escuderias(request):
        todas_las_escuderias = Escuderias.objects.all()
        context = {
        'escuderias': todas_las_escuderias,
        }
        return render(request,'pagina_escuderias.html', context = context)

def lista_circuitos(request):
        todos_los_circuitos = Circuitos.objects.all()
        context = {
        'circuitos': todos_los_circuitos,
        }
        return render(request,'pagina_circuitos.html', context = context)