from django.contrib import admin

from .models import Producto

class ListarProductos(admin.ModelAdmin):
	list_display = ['codigo','descripcion','precio','departamento','grupo','clasificacion',]

admin.site.register(Producto,ListarProductos)