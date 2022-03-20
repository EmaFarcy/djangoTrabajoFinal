from django import forms

class CicloturistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=50)
    contado= forms.BooleanField(required=False)

class CicloturistaBusqueda(forms.Form):
    nombre= forms.CharField(max_length=20)

class CorredorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=50)
    equipo= forms.CharField(max_length=60)

class CorredorBusqueda(forms.Form):
    nombre= forms.CharField(max_length=20)
    
class RutaFormulario(forms.Form):
     marca = forms.CharField(max_length=60)
     modelo = forms.CharField(max_length=60)