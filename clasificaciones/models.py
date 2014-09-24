from django.db import models

# Clasificaciones como: PACA NUEVA, PACA USADA, ETC.
class Clasificacion(models.Model):
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.descripcion