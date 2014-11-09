
from django.shortcuts import render

from django.http import Http404

from .models import Producto
from .serializers import ProductoSerializer,ProdDispSerializer
from inventarios.models import Inventario

from rest_framework.views import APIView
from rest_framework.response import Response

import datetime

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
		now = datetime.datetime.now()
		now = now.strftime('%d-%m-%Y')

		producto = Producto.objects.get(codigo=Prod)	
		disponible = Inventario.objects.filter(producto=producto) #.filter(fecha__gt=now)
		
		response = self.serialized_proddisp(disponible,many=True)
		return Response(response.data)