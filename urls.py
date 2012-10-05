from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$','frontend.views.inicio'),
    url(r'^usuarios/$','frontend.views.usuarios'),
    url(r'^recetas/$','frontend.views.lista_recetas'),
    url(r'^receta/(?P<id_receta>\d+)$', 'frontend.views.detalle_receta'),
    url(r'^sobre/$','frontend.views.sobre'),    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
                    {'document_root':settings.MEDIA_ROOT,}
        ),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

