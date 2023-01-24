from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DeleteView

from Tienda.models import Productos
from Tienda.forms import ProductoForm

def pagina_inicio(request):
    return render(request, 'Tienda/pagina_inicio.html', context={})


def lista_productos(request):
    producto = Productos.objects.all()
    context = {
        'producto': producto
    }
    return render(request, 'Tienda/lista_productos.html', context=context)

class ProductosListView(ListView):
    model = Productos
    template_name = 'Tienda/lista_productos.html'



def crear_producto(request):
    if request.method == 'GET':
        context = {
            'form': ProductoForm()
        }
        return render(request, 'Tienda/crear_producto.html', context=context)

    elif request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            Productos.objects.create(
                nombre = form.cleaned_data['nombre'],
                talla = form.cleaned_data['talla'],
                precio = form.cleaned_data['precio'],
                stock = form.cleaned_data['stock']
            )
            context = {
                'mensaje': 'Prenda creada correctamente'
            }
            return render (request, 'Tienda/crear_producto.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form' : ProductoForm()
            }
            return render (request, 'Tienda/crear_producto.html', context=context)

class ProductosCreateView(CreateView):
    model = Productos
    template_name = 'Tienda/crear_producto.html'
    fields = '__all__'
    success_url = '/Tienda/lista-productos/'



def modificar_producto(request, pk):
    producto = get_object_or_404(Productos, pk = pk)
    
    context = {
            'form': ProductoForm()
        }

    if request.method == 'POST':
        form = ProductoForm(context = request.POST)
        if form.is_valid():
                producto.save()
                return redirect (to = 'Tienda/modificar_producto.html')
        context['form'] = form
    
    return render (request, 'Tienda/modificar_producto.html', context=context)



class ProductosDeleteView(DeleteView):
    model = Productos
    template_name = 'Tienda/eliminar_producto.html'
    success_url = '/Tienda/lista-productos/'
