from django.db import models

from grupos.models import Grupo
from clasificaciones.models import Clasificacion
from departamentos.models import Departamento

class Producto(models.Model):
	codigo = models.CharField(max_length=10)
	descripcion = models.CharField(max_length=150)
	precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True)

	grupo = models.ForeignKey(Grupo, related_name='grupos_rel')
	clasificacion = models.ForeignKey(Clasificacion)
	departamento = models.ForeignKey(Departamento)

	def __unicode__(self):
		return "%s" % self.descripcion