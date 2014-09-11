from django.db import models

from productos.models import Producto

class Factura(models.Model):
	facturas_choices = (('A','Activa'),('I','Inactiva'),)
	facturas_impresa = (('S','SI'),('N','NO'),)

	no_factura = models.IntegerField()
	fecha = models.DateTimeField(auto_now_add=True)
	estatus = models.CharField(max_length=1, choices=facturas_choices)
	impresa = models.CharField(max_length=1, choices=facturas_impresa)

class Detalle(models.Model):
	
	producto = models.ForeignKey(Producto)
	descuento = models.IntegerField(blank=True)
	cantidad = models.PositiveIntegerField()
	precio = models.PositiveIntegerField()
	factura = models.ForeignKey(Factura)

	def __unicode__(self):
		return u"%s %s" % (self.producto, (self.cantidad * self.precio))