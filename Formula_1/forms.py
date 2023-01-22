from django import forms

class PilotoForm(forms.Form):
    nombre = forms.CharField(max_length=70)
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length=30)

class EscuderiaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    nacionalidad = forms.CharField(max_length=30)
    sede = forms.CharField(max_length=50)
    año_de_fundacion = forms.IntegerField()

class CircuitosForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    ubicacion = forms.CharField(max_length=100)
    longitud = forms.CharField(max_length=20)
    capacidad = forms.CharField(max_length=35)
