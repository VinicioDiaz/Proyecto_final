from django.shortcuts import render
from django.http import HttpResponse

from Formula_1.models import Pilotos, Escuderias, Circuitos, Posicion_pilotos_2022, Posicion_constructores_2022
from Formula_1.forms import PilotoForm, EscuderiaForm, CircuitosForm


def crear_piloto(request):
    if request.method == 'GET':
        context = {
            'form': PilotoForm()
        }
        return render(request, 'crear_piloto.html', context=context)

    elif request.method == 'POST':
        form = PilotoForm(request.POST)
        if form.is_valid():
            Pilotos.objects.create(
                nombre = form.cleaned_data['nombre'],
                edad = form.cleaned_data['edad'],
                nacionalidad = form.cleaned_data['nacionalidad'],
            )
            context = {
                'mensaje': 'Piloto creado correctamente'
            }
            return render (request, 'crear_piloto.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form' : PilotoForm()
            }
            return render (request, 'crear_piloto.html', context=context)

def crear_escuderia(request):
    nueva_escuderia = Escuderias.objects.create(nombre = 'Oracle Red Bull Racing', nacionalidad = 'Inglesa' , sede = 'Milton Keynes, England, UK' , año_de_fundacion = 2005)
    return HttpResponse("Haz creado una nueva escunderia")

def crear_circuito(request):
    nuevo_circuito = Circuitos.objects.create(nombre = 'Circuito de Barcelona-Cataluña', ubicacion = 'Cataluña, España' , longitud = '4,675 km' , capacidad = '140,700 espectadores')
    return HttpResponse("Haz creado un nuevo circuito")

def clasificacion_pilotos(request):
    lista_clasificacion_pilotos = Posicion_pilotos_2022.objects.create(posicion = '1', conductor = 'Max Verstappen', nacionalidad = 'NED', auto = 'Red Bull Racing RBPT', puntos = '454 pts')
    return HttpResponse("Agregaste piloto a la clasificación")

def clasificacion_constructores(request):
    lista_clasificacion_constructores = Posicion_constructores_2022.objects.create(posicion = '1', equipo = 'Red Bull Racing RBPT', puntos = '759 pts')
    return HttpResponse("Agregaste constructor a la clasificación")






def pagina_de_inicio(request):
    return render(request, 'pagina_inicio.html', context={})

def lista_pilotos(request):
    if 'search' in request.GET:
        search = request.GET['search']
        todos_los_pilotos = Pilotos.objects.filter(name__icontains=search)
    else:
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

def Posicion_mundial_piloto(request):
    todas_las_posiciones = Posicion_pilotos_2022.objects.all()
    context = {
        'posiciones': todas_las_posiciones,
    }
    return render (request,'clasificacion-pilotos.html', context = context)

def Posicion_mundial_constructor(request):
    todas_las_posiciones = Posicion_constructores_2022.objects.all()
    context = {
        'posiciones': todas_las_posiciones,
    }
    return render (request,'clasificacion-constructores.html', context = context)