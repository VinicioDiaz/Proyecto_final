from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Tienda.models import Productos
from Tienda.forms import ProductoForm

def pagina_inicio(request):
    return render(request, 'Tienda/pagina_inicio.html', context={})

def comprar_producto(request):
    return render(request, 'Tienda/comprar_producto.html', context={})


def lista_productos(request):
    producto = Productos.objects.all()
    context = {
        'producto': producto
    }
    return render(request, 'Tienda/lista_productos.html', context=context)

class ProductosListView(LoginRequiredMixin, ListView):
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

class ProductosCreateView(LoginRequiredMixin, CreateView):
    model = Productos
    template_name = 'Tienda/crear_producto.html'
    fields = '__all__'
    success_url = '/Tienda/lista-productos/'



def modificar_producto(request, pk):
    producto = Productos.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': ProductoForm(
                initial={
                    'nombre': producto.nombre,
                    'talla': producto.talla,
                    'precio': producto.precio,
                    'stock': producto.stock,
                }
            )
        }
        return render (request, 'Tienda/modificar_producto.html', context=context)

    elif request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto.nombre = form.cleaned_data['nombre']
            producto.talla = form.cleaned_data['talla']
            producto.precio = form.cleaned_data['precio']
            producto.stock = form.cleaned_data['stock']
            producto.save()

            context = {
                'mensaje': 'Producto actualizado exitosamente'
            }
    
    else:
        context = {
            'form_errors': form.errors,
            'form': ProductoForm()
        }
    return render(request, 'Tienda/modificar_producto.html', context=context)

class ProductosUpdateView(LoginRequiredMixin, UpdateView):
    model = Productos
    template_name = 'Tienda/modificar_producto.html'
    fields = '__all__'
    success_url = '/Tienda/lista-productos/'


class ProductosDeleteView(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = 'Tienda/eliminar_producto.html'
    success_url = '/Tienda/lista-productos/'
