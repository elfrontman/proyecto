from models import *
from django.contrib import admin
from picasa import PicasaAdminImageWidget

class ImageWidget(PicasaAdminImageWidget):
	SIZE='48'

class ImageAdmin(admin.ModelAdmin):
	formfield_overrides = {PicasaField:{'widget':PicasaAdminImageWidget},}

admin.site.register(Receta)
admin.site.register(Comentario)
admin.site.register(Image, ImageAdmin)