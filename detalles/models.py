from django.db import models

from productos.models import Producto

class Detalle(models.Model):
	
	producto = models.ForeignKey(Producto)
	descuento = models.IntegerField(blank=True)
	cantidad = models.PositiveIntegerField()
	precio = models.PositiveIntegerField()
	# factura = models.ForeignKey(Factura)

	def __unicode__(self):
		return u"%s %s" % (self.producto, (self.cantidad * self.precio))