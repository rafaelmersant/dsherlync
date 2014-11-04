# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import Http404, HttpResponse, QueryDict
from django.views.generic import View, ListView, DetailView
from django.db.models import Sum, Count

from datetime import date

import datetime

import json
import math

from .models import Factura, Detalle
from productos.models import Producto


class BuscarFactura(ListView):
	
	template_name = 'buscarfactura.html'
	model = Factura


class FacturasDelDia(ListView):

	template_name = 'facturasdeldia.html'
	model = Detalle

	def get(self, request, *args, **kwargs):
		if self.request.GET.get('Fecha'):
			parametro = self.request.GET.get('Fecha')
			queryset = Detalle.objects.filter(factura__fecha__contains=parametro).annotate(totalgeneral=Sum('precio'),descuentos=Sum('descuento')).order_by('-factura__fecha')
		else:
			queryset = Detalle.objects.values('factura_id').annotate(totalgeneral=Sum('precio'),descuentos=Sum('descuento')).order_by('-factura__fecha')

		self.object_list = queryset
		context = self.get_context_data()

		return self.render_to_response(context)


class FacturarView(View):

	def get(self, request, *args, **kwargs):
		try:
			return HttpResponse('This is a GET')
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

			return HttpResponse(next_factura)

		except Exception as e:
			return HttpResponse(e)


def index(request):
	return render(request, 'regfactura.html')

def apartados(request):
	return render(request, 'apartados.html')