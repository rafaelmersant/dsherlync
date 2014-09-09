from django.db import models

from grupos.models import Grupo
from clasificaciones.models import Clasificacion

class Producto(models.Model):
	codigo = models.CharField(max_length=10)
	descripcion = models.CharField(max_length=150)
	precio = models.DecimalField(max_digits=12, decimal_places=2)

	grupo = models.ForeignKey(Grupo)
	clasificacion = models.ForeignKey(Clasificacion)

	def __unicode__(self):
		return self.descripcion