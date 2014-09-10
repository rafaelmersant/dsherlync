from django.contrib import admin

from .models import Factura
from detalles.models import Detalle

class DetalleInline(admin.StackedInline):
	model = Detalle
	extra = 1

# admin.site.register(Factura)