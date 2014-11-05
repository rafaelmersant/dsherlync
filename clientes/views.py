from django.shortcuts import render

from .models import Cliente
from .serializers import ClienteSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class ClienteListView(APIView):

	serialized_cliente = ClienteSerializer

	def get(self, request, nombre=None, format=None):
		if nombre != None:
			clientes = Cliente.objects.filter(nombre__contains=nombre)
		else:
			clientes = Cliente.objects.all()

		response = self.serialized_cliente(clientes,many=True)
		return Response(response.data)