from .models import Producto
from grupos.models import Grupo
from clasificaciones.models import Clasificacion

from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = ('id','codigo','descripcion',
			'precio',
			'grupo',
			'clasificacion',
			'departamento'
			)

class GrupoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Grupo
		fields = ('id','descripcion_grupo',)
