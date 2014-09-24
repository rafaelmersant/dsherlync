from django.db import models

# Ropas: BLUSAS, PANTALONES, ETC.
class Grupo(models.Model):
	descripcion_grupo = models.CharField(max_length=100)

	def __unicode__(self):
		return self.descripcion_grupo