#encoding:utf-8
import os, sys
from django.db import models
from django.contrib.auth.models import User
from picasa import PicasaField

def get_Album(instance, filename):
	album = str(instance.album)
	return os.path.join(album,filename)

def choices():
	from picasa import PicasaStorage
	storage = PicasaStorage()
	return [(a.title.text, a.title.text) for a in storage.albumsFromUser()]

class Album(models.Model):
	name = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name


class Image(models.Model):
	album = models.CharField(max_length=50, choices = choices())
	mediaFoto = PicasaField(upload_to=get_Album)
	dropBoxFoto = PicasaField()

	def __unicode__(self):
		return self.dropBoxFoto.url


class Receta(models.Model):
	#Dato cadena, longitud 100 y unico
	titulo = models.CharField(max_length=100, unique=True)
	#Dato Texto, con texto de ayuda
	ingredientes = models.TextField(help_text='Redacta los ingredientes')
	#Dato Texto, con nombre: Preparacion
	preparacion = models.TextField(verbose_name='Preparacion')
	#Dato Imagen, se almacenta en la carptea recetas, titulo: Imagen
	imagen = models.ImageField(upload_to='recetas', verbose_name='Imagen')
	#Dato Fecha y Hora, almacena la fecha y hora actual
	tiempo_registro = models.DateTimeField(auto_now=True)
	#Enlace al modelo que Django ya tiene construido
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
	receta = models.ForeignKey(Receta)
	texto = models.TextField(help_text='Tu Comentario', verbose_name='Comentario')

	def __unicode__(self):
		return self.texto
		