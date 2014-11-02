from django.shortcuts import render
from django.http import Http404, HttpResponse, QueryDict
from django.views.generic import View, ListView
from django.db.models import Sum, Count

import datetime

import json
import math

from .models import Factura, Detalle
from productos.models import Producto


class FacturasDelDia(ListView):

	template_name = 'facturasdeldia.html'
	model = Detalle

	def get_queryset(self):
		if self.kwargs.get('Fecha'):
			# super(FacturasDelDia,self)
			# queryset = super(FacturasDelDia, self).get_queryset().filter(factura=221)
			queryset = Detalle.objects.filter(factura=21)
			
		else:
			queryset = Detalle.objects.filter(factura=221)

			# queryset = super(FacturasDelDia, self).get_queryset().raw('select id, factura_id, sum(precio*cantidad) - descuento importeLine' 
				# + ' from facturas_detalle group by factura_id order by factura_id desc')
			# queryset = super(FacturasDelDia, self).get_queryset().values('factura').order_by('-factura').annotate(Sum('precio'))

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
			items = request.body

			next_factura = Factura.objects.latest('pk').no_factura + 1
			
			factura = Factura()
			factura.no_factura = next_factura
			factura.save()
			
			for item in data['items']:
				codigo = item['Codigo'].strip()
				cantidad = item['Cantidad']
				descuento = float(item['Descuento'])
				precio = item['Precio']

				if descuento == '':
					descuento = '0'

				detalle = Detalle()
				detalle.producto = Producto.objects.get(codigo=codigo)
				detalle.cantidad = cantidad
				detalle.descuento = descuento
				detalle.precio = precio
				detalle.factura = Factura.objects.get(no_factura=next_factura)
				detalle.save()

			return HttpResponse(1)

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