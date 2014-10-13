
from django.shortcuts import render

from django.http import Http404

from .models import Producto
from .serializers import ProductoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class ProductoListView(APIView):

	serialized_producto = ProductoSerializer

	def get(self, request, descrp=None, format=None):
		if descrp != None:
			productos = Producto.objects.filter(descripcion__contains=descrp)	
		else:
			productos = Producto.objects.all()

		response = self.serialized_producto(productos,many=True)
		return Response(response.data)