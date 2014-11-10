
from django.shortcuts import render

from django.http import Http404, HttpResponse

from .models import Producto
from .serializers import ProductoSerializer,ProdDispSerializer
from inventarios.models import Existencia

from rest_framework.views import APIView
from rest_framework.response import Response

import datetime
import json

class ProductoListView(APIView):

	serialized_producto = ProductoSerializer

	def get(self, request, descrp=None, format=None):
		if descrp != None:
			productos = Producto.objects.filter(descripcion__contains=descrp)	
		else:
			productos = Producto.objects.all()

		response = self.serialized_producto(productos,many=True)
		return Response(response.data)

class ProductoDisponibleView(APIView):

	serialized_proddisp = ProdDispSerializer

	def get(self, request, Prod=None, format=None):

		disponible = Existencia()
		nodisp = {}

		try:
			producto = Producto.objects.get(codigo=Prod)	
			disponible = Existencia.objects.get(producto=producto)
		
			response = self.serialized_proddisp(disponible,many=False)
		except disponible.DoesNotExist:
			nodisp['cantidad'] = '0'
			response = json.dumps(nodisp)
			return HttpResponse(response)
	
		return Response(response.data)