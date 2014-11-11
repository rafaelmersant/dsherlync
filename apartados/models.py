from django.db import models
from productos.models import Producto
from clientes.models import Cliente

from datetime import datetime, timedelta

class Apartado(models.Model):
	estatus_choices = (('A','Activo'),('X','Anulado'),('C','Completado'))

	no_apartado = models.IntegerField()
	fecha = models.DateField(auto_now_add=True)
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField()
	precio = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
	fecha_vence = models.DateField(default=datetime.now()+timedelta(days=15))
	estatus = models.CharField(max_length=1, choices=estatus_choices,
							   default=estatus_choices[0][0])


class DeudaCliente(models.Model):

	cliente = models.ForeignKey(Cliente)
	deuda = models.DecimalField(max_digits=8, decimal_places=2)

	def __unicode__(self):
		return '%s' % (self.cliente)


class AbonoCliente(models.Model):

	cliente = models.ForeignKey(Cliente)
	abono = models.DecimalField(max_digits=8, decimal_places=2)
	fecha = models.DateField(auto_now_add=True)