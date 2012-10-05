from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$','proyecto.frontend.views.inicio'),
    url(r'^usuarios/$','proyecto.frontend.views.usuarios'),
    url(r'^recetas/$','proyecto.frontend.views.lista_recetas'),
    url(r'^receta/(?P<id_receta>\d+)$', 'proyecto.frontend.views.detalle_receta'),
    url(r'^sobre/$','proyecto.frontend.views.sobre'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
                    {'document_root':settings.MEDIA_ROOT,}
        ),
    url(r'^contacto/$','proyecto.frontend.views.contacto'),
    url(r'^receta/nueva$','proyecto.frontend.views.nueva_receta'),
    url(r'^comenta/$','proyecto.frontend.views.nuevo_comentario'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

