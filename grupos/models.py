from django.db import models

class Grupo(models.Model):
	descripcion_grupo = models.CharField(max_length=100, verbose_name='HOLA GRUPO')

	class Meta:
		# app_label = "Grupo"
		verbose_name = "Group"
		verbose_name_plural = "Groups"

	def __unicode__(self):
		return self.descripcion_grupo