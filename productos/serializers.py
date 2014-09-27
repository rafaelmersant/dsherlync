from .models import Producto
from grupos.models import Grupo
from clasificaciones.models import Clasificacion

from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
	grupo = serializers.RelatedField(many=False)
	clasificacion = serializers.RelatedField(many=False)
	departamento = serializers.RelatedField(many=False)

	class Meta:
		model = Producto
		fields = ('id','codigo','descripcion',
			'precio',
			'grupo',
			'clasificacion',
			'departamento',
			)