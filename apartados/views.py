from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import ListView, View

from .forms import ClienteForm

from clientes.models import Cliente
from apartados.models import Apartado, DeudaCliente, AbonoCliente
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

			if Apartado.objects.count() > 0:
				next_apartado = Apartado.objects.latest('pk').no_apartado + 1
			else:
				next_apartado = 1
			
			apartado = Apartado()
			apartado.no_apartado = next_apartado
			
			cliente = data['cliente']
			abono = data['abono']

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

				existencia = Existencia()
				try:
					existencia = Existencia.objects.get(producto=apartado.producto)
					existencia.cantidad -= cantidad
					existencia.save()

				except existencia.DoesNotExist:
					raise Exception('No tiene el producto ' + apartado.producto.descripcion + ' en Existencia.')		

			if abono:
				abonoCte = AbonoCliente()
				abonoCte.cliente = apartado.cliente
				abonoCte.abono = float(abono)
				abonoCte.save()
				total_deuda = total_deuda - float(abono)

			deudaCte = DeudaCliente()
			deudaCte.cliente = Cliente.objects.get(pk=cliente)
			deudaCte.deuda = total_deuda
			deudaCte.save()

			return HttpResponse(next_apartado)

		except Exception as e:
			return HttpResponse(e)


class AbonarCuentaView(ListView):

	template_name = 'abonarcuenta.html'
	model = AbonoCliente

	def get(self, request, *args, **kwargs):
		if self.request.GET.get('cliente'):
			parametro = self.request.GET.get('cliente')

			cliente = Cliente.objects.get(nombre=parametro)
			queryset = DeudaCliente.objects.filter(cliente=cliente)
		else:
			queryset = None

		self.object_list = queryset
		context = self.get_context_data()

		return self.render_to_response(context)