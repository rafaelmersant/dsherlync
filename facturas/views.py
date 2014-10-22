from django.shortcuts import render
from django.http import Http404, HttpResponse, QueryDict
from django.views.generic import View


import json

from .models import Factura, Detalle


class FacturarView(View):

	def get(self, request, *args, **kwargs):
		try:
			return HttpResponse('This is a GET para ROMPER JAJAJAJA')
		except Exception as e:
			return HttpResponse(e)

	def post(self, request, *args, **kwargs):
		try:
			# items = json.loads(request.POST.get('items'))
			
			items = request.POST.get('itemsToAdd') 
			# data = json.parse(items)
			# data = items['itemsToAdd']

			return HttpResponse(items)

		except Exception as e:
			return HttpResponse(e)



def index(request):
	return render(request, 'regfactura.html')

def apartados(request):
	return render(request, 'apartados.html')

# def AgregarFactura(request, id_factura):
# 	if id_factura == 0:
# 		fact = Factura.objects.get(pk=id_factura)
# 	else:
# 		fact = Factura.save()

	
# class AgregarFactura(request):

# 	def get(self, request, descrp=None, format=None):
# 		if descrp != None:
# 			productos = Producto.objects.filter(descripcion__contains=descrp)	
# 		else:
# 			productos = Producto.objects.all()

# 		response = self.serialized_producto(productos,many=True)
# 		return Response(response.data)