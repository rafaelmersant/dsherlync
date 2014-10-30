from django.contrib import admin

from .models import Factura, Detalle

class DetalleViewAdmin(admin.ModelAdmin):
	list_display = ['pk','producto','descuento','cantidad','precio','factura']

admin.site.register(Factura)
admin.site.register(Detalle,DetalleViewAdmin)