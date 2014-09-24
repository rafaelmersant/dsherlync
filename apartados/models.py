from django.db import models
from productos.models import Producto
from clientes.models import Cliente

from datetime import datetime, timedelta

class Apartado(models.Model):
	estatus_choices = (('A','Activo'),('X','Anulado'))

	fecha = models.DateTimeField(auto_now_add=True)
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField()
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	fecha_vence = models.DateTimeField(default=datetime.now()+timedelta(days=15))

	def __unicode__(self):
		return "Producto: %s - Cantidad: " % (self.producto.descripcion, self.cantidad)