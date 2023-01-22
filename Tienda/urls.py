from django.urls import path
from Tienda.views import pagina_de_inicio

urlpatterns = [

    path('pagina-inicio/', pagina_de_inicio),

]