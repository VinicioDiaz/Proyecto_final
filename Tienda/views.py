from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def pagina_de_inicio(request):
    return render(request, 'Base.html', context={})