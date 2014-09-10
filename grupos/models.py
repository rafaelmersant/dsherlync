from django.db import models

class Grupo(models.Model):
	descripcion_grupo = models.CharField(max_length=100, verbose_name='Grupo')

	class Meta:
		# app_label = "Grupo"
		verbose_name = "Grupo"
		verbose_name_plural = "Grupos"

	def __unicode__(self):
		return self.descripcion_grupo