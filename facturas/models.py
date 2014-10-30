from django.db import models

from productos.models import Producto

class Factura(models.Model):
	
	facturas_choices = (('A','Activa'),('I','Inactiva'),)
	facturas_impresa = (('S','SI'),('N','NO'),)

	no_factura = models.IntegerField()
	fecha = models.DateTimeField(auto_now_add=True)
	estatus = models.CharField(max_length=1, choices=facturas_choices, default='A')
	impresa = models.CharField(max_length=1, choices=facturas_impresa, default='N')

	def __unicode__(self):
		return u'%i %s' % (self.no_factura,str(self.fecha.strftime('%d/%m/%Y')))

class Detalle(models.Model):
	
	producto = models.ForeignKey(Producto)
	descuento = models.IntegerField(blank=True, default=0)
	cantidad = models.PositiveIntegerField()
	precio = models.PositiveIntegerField()
	factura = models.ForeignKey(Factura)

	def _get_total(self):
		return '%i' % (self.cantidad * self.precio)

	total = property(_get_total)

	def __unicode__(self):
		return u"%s %s" % (self.producto, (self.cantidad * self.precio))