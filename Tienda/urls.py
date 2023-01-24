from django.urls import path
from Tienda.views import pagina_inicio, lista_productos, crear_producto, modificar_producto, ProductosListView, ProductosCreateView, ProductosDeleteView


urlpatterns = [

    path('pagina-inicio/', pagina_inicio, name = 'pagina_inicio'),
    path('lista-productos/', ProductosListView.as_view(), name = 'lista_productos'),
    path('crear-producto/', ProductosCreateView.as_view(), name = 'crear_producto'),
    path('modificar-producto/<int:pk>/', modificar_producto, name = 'modificar_producto'),
    path('eliminar-producto/<int:pk>/', ProductosDeleteView.as_view(), name = 'eliminar_producto'),

]