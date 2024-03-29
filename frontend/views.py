#encode:utf-8
from proyecto.frontend.models import Receta, Comentario, Image
from proyecto.frontend.forms import RecetaForm, ComentarioForm, ContactoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def images(request):
	return render_to_response('images.html', {'images':Image.objects})

def sobre(request):
	html = "<html><body>Proyecto de Ejemple en Django<body></html>"
	return HttpResponse(html)

def inicio(request):
	recetas = Receta.objects.all()
	return render_to_response('inicio.html',{'recetas':recetas}, context_instance=RequestContext(request))

def usuarios(request):
	usuarios = User.objects.all()
	recetas = Receta.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios,'recetas':recetas}, context_instance=RequestContext(request))

def lista_recetas(request):
	recetas = Receta.objects.all()
	return render_to_response('recetas.html',{'datos':recetas},context_instance=RequestContext(request))

def detalle_receta(request, id_receta):
	dato = get_object_or_404(Receta, pk=id_receta)
	comentario = Comentario.objects.filter(receta=dato)
	return render_to_response('receta.html',{'receta':dato,'comentario':comentario},context_instance=RequestContext(request))

def contacto(request):
	if request.method == 'POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje desde el recetario de Proyecto'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comuniquese a: '+ formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['tcarlosvargas@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactoForm()
	return render_to_response('contactoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def nueva_receta(request):
	if request.method == 'POST':
		formulario = RecetaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/recetas')
	else:
		formulario = RecetaForm()

	return render_to_response('recetaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_comentario(request):
	if request.method == 'POST':
		formulario = ComentarioForm()
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/recetas')
	else:
		formulario = ComentarioForm()
	return render_to_response('comentarioform.html',{'formulario':formulario},context_instance=RequestContext(request))

def nuevo_usuario(request):
	if(request.method == 'POST'):
		formulario = UserCreationForm(request.POST)
		if(formulario.is_valid):
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuarios = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuarios, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
		return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')				
def privado(request):
	usuario = request.user
	return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')	
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')






			