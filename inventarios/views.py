from django.shortcuts import render

from facturas.models import Factura, Detalle
from .models import Inventario

def CantidadDisponibleProducto(producto):
	vendidos = Factura.objects.filter(fecha)

	
def CantidadDisponible(request):
	