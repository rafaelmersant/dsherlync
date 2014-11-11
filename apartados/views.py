from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import ListView, View, TemplateView

from .forms import ClienteForm

from clientes.models import Cliente
from apartados.models import Apartado, DeudaCliente, AbonoCliente
from inventarios.models import Movimiento, Existencia
from productos.models import Producto

from .serializers import AbonoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

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
		try:

			if self.request.GET.get('cliente'):
				parametro = self.request.GET.get('cliente')

				deuda = DeudaCliente()
				try:

					cliente = Cliente.objects.get(pk=parametro)
					deuda = DeudaCliente.objects.get(cliente=cliente).deuda
				except DeudaCliente.DoesNotExist:
					queryset = None

				if deuda <= 0:
					queryset = None
				else:
					queryset = DeudaCliente.objects.filter(cliente=cliente)
			else:
				queryset = None

			self.object_list = queryset
			context = self.get_context_data()

			return self.render_to_response(context)

		except Exception as e:
			return HttpResponse(e)

class AbonoListView(APIView):

	serialized_abono = AbonoSerializer

	def get(self, request, cliente=None, format=None):
		if cliente != None:
			o_cliente = Cliente.objects.filter(id=cliente)
			abonos = AbonoCliente.objects.filter(cliente=o_cliente)
		else:
			abonos = None

		response = self.serialized_abono(abonos,many=True)
		return Response(response.data)


class AbonarMontoView(View):

	template_name = "abonarcuenta.html"

	def post(self, request, *args, **kwargs):
		try:

			data = json.loads(request.body)
			
			cliente = data['cliente']
			montoAbono = data['abono']

			o_cliente = Cliente.objects.get(pk=cliente)

			abono = AbonoCliente()
			abono.cliente = o_cliente
			abono.abono = montoAbono
			abono.save()

			deudaCte = DeudaCliente.objects.get(cliente=abono.cliente)
			if montoAbono > deudaCte.deuda:
				raise Exception('El monto que intenta pagar esta por encima de la deuda.')
			else:
				deudaCte.deuda -= montoAbono
				deudaCte.save()

			if (deudaCte.deuda - montoAbono) == 0:
				apartados = Apartado.objects.filter(cliente=abono.cliente)
				apartados.estatus = 'C'
				apartados.save()

			return HttpResponse('El abono fue realizado!')

		except Exception as e:
			return HttpResponse(e)