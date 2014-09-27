from .models import Grupo

from rest_framework import serializers

class GrupoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Grupo
		fields = ('id','descripcion_grupo',)

