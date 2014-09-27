from .models import Producto

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

