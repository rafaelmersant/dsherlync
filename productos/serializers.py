from .models import Producto

from rest_framework import serializers

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = ('id','codigo','descripcion',
			'precio',
			'grupo',
			'clasificacion',
			'departamento'
			)

