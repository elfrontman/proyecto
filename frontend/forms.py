#encoding:utf-8
from django.forms import ModelForm
from django import forms
from proyecto.frontend.models import *

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class RecetaForm(ModelForm):
	class Meta:
		model = Receta

class ComentarioForm(ModelForm):
	class Meta:
		model = Comentario
