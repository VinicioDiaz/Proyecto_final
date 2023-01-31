from django.contrib.auth.views import LogoutView
from django.urls import path
from Usuarios.views import login_view, register


urlpatterns = [
    path ('login/', login_view, name='login'),
    path ('logout/', LogoutView.as_view(template_name = 'Usuarios/logout.html')),
    path ('signup/', register)

]