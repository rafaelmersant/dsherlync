from django.shortcuts import render

from .models import Producto
from .serializers import ProductoSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductoList(APIView):
	serialized_producto = ProductoSerializer

	def get(self, request, descrp=None, format=None):
		if descrp != None:
			productos = Producto.objects.filter(descripcion__contains=descrp)
		else:
			productos = Producto.objects.all()

		response = self.serialized_producto(productos,many=True)
		return Response(response.data)

productos_view = ProductoList.as_view()

# class ProductoDetail(APIView):

# 	def get_object(self, descrp):
# 		try:
# 			return Producto.object.get(descripcion__contains__(descrp))
# 		except Producto.DoesNotExists:
# 			raise Http404

# 	def get(self, request, descrp, format=None):
# 		producto = self.get_object(descrp)
# 		serialized_producto = ProductoSerializer(producto)
# 		return Response(serialized_producto.data)