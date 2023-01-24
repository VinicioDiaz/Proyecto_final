from django import forms


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    talla = forms.CharField(max_length=50)
    precio = forms.FloatField()
    stock = forms.BooleanField()
