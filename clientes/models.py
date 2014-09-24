from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	telefono = models.CharField(max_length=50)
	
	def __unicode__(self):
		return "%s - (%s)" % (self.nombre, self.telefono)