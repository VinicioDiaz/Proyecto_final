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
    if request.method == 'GET':
        context = {
            'form': EscuderiaForm()
        }
        return render(request, 'crear_escuderia.html', context=context)

    elif request.method == 'POST':
        form = EscuderiaForm(request.POST)
        if form.is_valid():
            Escuderias.objects.create(
                nombre = form.cleaned_data['nombre'],
                nacionalidad = form.cleaned_data['nacionalidad'],
                sede = form.cleaned_data['sede'],
                año_de_fundacion = form.cleaned_data['año_de_fundacion'],
            )
            context = {
                'mensaje': 'Escuderia creada correctamente'
            }
            return render (request, 'crear_escuderia.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form' : EscuderiaForm()
            }
            return render (request, 'crear_escuderia.html', context=context)


def crear_circuito(request):
    if request.method == 'GET':
        context = {
            'form': CircuitosForm()
        }
        return render(request, 'crear_circuito.html', context=context)

    elif request.method == 'POST':
        form = CircuitosForm(request.POST)
        if form.is_valid():
            Circuitos.objects.create(
                nombre = form.cleaned_data['nombre'],
                ubicacion = form.cleaned_data['ubicacion'],
                longitud = form.cleaned_data['longitud'],
                capacidad = form.cleaned_data['capacidad'],
            )
            context = {
                'mensaje': 'Circuito creado correctamente'
            }
            return render (request, 'crear_circuito.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form' : CircuitosForm()
            }
            return render (request, 'crear_circuitos.html', context=context)


def clasificacion_pilotos(request):
    lista_clasificacion_pilotos = Posicion_pilotos_2022.objects.create(posicion = '1', conductor = 'Max Verstappen', nacionalidad = 'NED', auto = 'Red Bull Racing RBPT', puntos = '454 pts')
    return HttpResponse("Agregaste piloto a la clasificación")

def clasificacion_constructores(request):
    lista_clasificacion_constructores = Posicion_constructores_2022.objects.create(posicion = '1', equipo = 'Red Bull Racing RBPT', puntos = '759 pts')
    return HttpResponse("Agregaste constructor a la clasificación")






def pagina_de_inicio(request):
    return render(request, 'pagina_inicio.html', context={})

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