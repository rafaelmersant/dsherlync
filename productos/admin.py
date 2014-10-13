from django.contrib import admin

from .models import Producto

class ListarProductos(admin.ModelAdmin):
	list_display = ['codigo','descripcion','precio','departamento','grupo','clasificacion',]
	list_editable = ('descripcion','precio','departamento','grupo','clasificacion')
	list_filter = ('departamento','grupo')
	search_fields = ('descripcion',)

admin.site.register(Producto,ListarProductos)