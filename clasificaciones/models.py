from django.db import models

class Clasificacion(models.Model):
	descripcion_c = models.CharField(max_length=100)

	def __unicode__(self):
		return self.descripcion_c