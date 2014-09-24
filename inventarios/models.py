# -*- coding: utf-8 -*-

from django.db import models

from productos.models import Producto

class Inventario(models.Model):
	tipo_inv_choices = (('E','Entrada'),('S','Salida'),)

	fecha_entrada = models.DateField(auto_now_add=True)
	tipo_inv = models.CharField(max_length=1, 
								choices=tipo_inv_choices, 
								default=tipo_inv_choices[0][0],
								verbose_name="Tipo de Inventario")
	descripcion_salida = models.CharField(max_length=255, blank=True, verbose_name="Descripción de Salida")
	producto = models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField()

	def __unicode__(self):
		return '%s == %s' % (self.producto.descripcion, self.cantidad)
