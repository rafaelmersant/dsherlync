from django.shortcuts import render, render_to_response

from django.http import HttpResponse
from django.views.generic.edit import FormView, View

from .forms import ClienteForm

from clientes.models import Cliente
from apartados.models import Apartado, DeudaCliente
from inventarios.models import Movimiento, Existencia
from productos.models import Producto

import json
import math

class ClienteFormView(FormView):
	template_name = "apartados.html"
	form_class = ClienteForm
	success_url = '/apartados'

	def form_valid(self, form):
		cte = form.save()

		return super(ClienteFormView, self).form_valid(form)


class ApartarView(View):

	template_name = "apartados.html"

	def post(self, request, *args, **kwargs):
		try:

			total_deuda = 0

			data = json.loads(request.body)

			next_apartado = Apartado.objects.latest('pk').no_apartado + 1
			
			apartado = Apartado()
			apartado.no_apartado = next_apartado
			
			cliente = data['cliente']

			for item in data['items']:
				codigo = item['Codigo'].strip()
				cantidad = float(item['Cantidad'])
				descuento = float(item['Descuento'])
				precio = float(item['Precio'])
				total_deuda += (cantidad * precio) - descuento

				if descuento == '':
					descuento = '0'

				apartado.cliente = Cliente.objects.get(pk=cliente)
				apartado.producto = Producto.objects.get(codigo=codigo)
				apartado.cantidad = cantidad
				apartado.descuento = descuento
				apartado.precio = precio
				apartado.save()

				mov = Movimiento()
				mov.producto = Producto.objects.get(codigo=codigo)
				mov.cantidad = cantidad
				mov.tipo_movimiento = 'S'
				mov.save()

				existencia = Existencia.objects.get(producto=apartado.producto)
				existencia.producto = Producto.objects.get(codigo=codigo)
				existencia.cantidad -= cantidad
				existencia.save()

			deudaCte = DeudaCliente()
			deudaCte.cliente = Cliente.objects.get(pk=cliente)
			deudaCte.deuda = total_deuda

			return HttpResponse(next_apartado)

		except Exception as e:
			return HttpResponse(e)

