# -*- coding: utf-8 -*-

from django.db import models

from productos.models import Producto
from datetime import datetime

class Inventario(models.Model):
	tipo_inv_choices = (('E','Entrada'),('S','Salida'),)

	fecha_entrada = models.DateField(default=datetime.now)
	tipo_inv = models.CharField(max_length=1, 
								choices=tipo_inv_choices, 
								default=tipo_inv_choices[0][0],
								verbose_name="Tipo de Inventario")
	producto = models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField()
	descripcion_salida = models.CharField(max_length=255, blank=True, verbose_name="Descripción de Salida")


class Movimiento(models.Model):
	tipo_mov_choices = (('E','Entrada'),('S','Salida'),)

	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()
	tipo_mov = models.CharField(max_length=1,
									   choices=tipo_mov_choices,
									   default=tipo_mov_choices[0][0],
									   ),
	fecha_movimiento = models.DateField(auto_now_add=True)


class Existencia(models.Model):

	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()
