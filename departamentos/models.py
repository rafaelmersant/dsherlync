from django.db import models


class Departamento(models.Model):
	descripcion = models.CharField(max_length=50)

	def __unicode__(self):
		return self.descripcion