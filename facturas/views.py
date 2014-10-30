from django.shortcuts import render
from django.http import Http404, HttpResponse, QueryDict
from django.views.generic import View, ListView
from django.db.models import Sum
import datetime

import json
import math

from .models import Factura, Detalle
from productos.models import Producto


class FacturasDelDia(ListView):

	template_name = 'facturasdeldia.html'
	model = Detalle

	def get_queryset(self):
		if self.kwargs.get('fecha'):
			super(FacturasDelDia,self)
			queryset = Detalle.objects.filter(factura__fecha__year = self.kwargs.get('fecha')) #filter(factura=self.kwargs.get('fecha')).aggregate(Sum('precio'))
		else:
			queryset = super(FacturasDelDia, self).get_queryset().order_by('-factura')

		return queryset


class FacturarView(View):

	def get(self, request, *args, **kwargs):
		try:
			return HttpResponse('This is a GET para ROMPER JAJAJAJA')
		except Exception as e:
			return HttpResponse(e)


	def post(self, request, *args, **kwargs):
		try:

			data = json.loads(request.body)

			next_factura = Factura.objects.latest('pk').no_factura + 1
			
			factura = Factura()
			factura.no_factura = next_factura
			factura.save()

			toma = ''
			for item in data:
				codigo = 'CAM01' #item['Codigo']
				cantidad = 1 #item['Codigo']
				descuento = 0 #item['Descuento']
				precio = 200 #item['Precio']

				toma = item['Codigo']

				detalle = Detalle()
				detalle.producto = Producto.objects.get(codigo=codigo)
				detalle.cantidad = cantidad
				detalle.descuento = descuento
				detalle.precio = precio
				detalle.factura = Factura.objects.get(no_factura=next_factura)
				detalle.save()

			return HttpResponse(toma)

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