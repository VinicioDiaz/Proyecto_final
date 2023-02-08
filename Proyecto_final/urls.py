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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include   

from Proyecto_final.settings import MEDIA_ROOT, MEDIA_URL
from Proyecto_final.views import pagina_de_inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_de_inicio, name='index'),
    path('pagina-inicio/', pagina_de_inicio),
    path('Formula_1/', include('Formula_1.urls')),
    path('Tienda/', include('Tienda.urls')),
    path('Usuarios/', include('Usuarios.urls'))


] + static(MEDIA_URL, document_root = MEDIA_ROOT)
