from django.http import HttpResponse 
from django.shortcuts import render


def pagina_de_inicio(request):
    return render(request, 'Pagina_inicio.html', context={})
