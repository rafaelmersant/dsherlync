from .models import Producto
from grupos.models import Grupo
from clasificaciones.models import Clasificacion
from inventarios.models import Inventario

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

class ProdDispSerializer(serializers.ModelSerializer):
	producto = serializers.RelatedField(many=False)

	class Meta:
		model = Inventario
		fields = ('producto','cantidad',)
