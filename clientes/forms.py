from django import forms

class CicloturistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=50)
    contado= forms.BooleanField(required=False)

class CicloturistaBusqueda(forms.Form):
    nombre= forms.CharField(max_length=20)
    
    