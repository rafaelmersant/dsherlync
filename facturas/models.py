from django.db import models

from productos.models import Producto
from detalles.models import Detalle

class Factura(models.Model):
	facturas_choices = (('A','Activa'),('I','Inactiva'),)
	facturas_impresa = (('S','SI'),('N','NO'),)

	no_factura = models.IntegerField()
	fecha = models.DateTimeField(auto_now_add=True)
	estatus = models.CharField(max_length=1, choices=facturas_choices)
	impresa = models.CharField(max_length=1, choices=facturas_impresa)
	detalle = models.ForeignKey(Detalle)
