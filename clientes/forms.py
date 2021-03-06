from django import forms
from ckeditor.fields import RichTextFormField

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
     caracteristicas = RichTextFormField(required= False)
     imagen_ruta= forms.ImageField(required= False)

class MtbFormulario(forms.Form):
     marca = forms.CharField(max_length=60)
     modelo = forms.CharField(max_length=60)
     caracteristicas = RichTextFormField(required= False)
     imagen_mtb= forms.ImageField(required= False)

class UrbanaFormulario(forms.Form):
     marca = forms.CharField(max_length=60)
     modelo = forms.CharField(max_length=60)
     caracteristicas = RichTextFormField(required= False)
     imagen_urbana= forms.ImageField(required= False)