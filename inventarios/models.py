# -*- coding: utf-8 -*-

from django.db import models

from productos.models import Producto

class Inventario(models.Model):
	tipo_inv_choices = (('E','Entrada'),('S','Salida'),)

	fecha_entrada = models.DateField(auto_now_add=True)
	tipo_inv = models.CharField(max_length=1, 
								choices=tipo_inv_choices, 
								default=tipo_inv_choices[0][0])

	producto = models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField()

	def __unicode__(self):
		return '%s ' % self.fecha_entrada
