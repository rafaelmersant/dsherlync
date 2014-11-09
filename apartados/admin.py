from django.contrib import admin

from .models import Apartado

class ApartadoAdmin(admin.ModelAdmin):
	list_display = ['id','cliente','producto','cantidad','precio','fecha','fecha_vence']

admin.site.register(Apartado,ApartadoAdmin)