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
from facturas.models import Factura, Detalle

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

			total_deuda = float(0)

			data = json.loads(request.body)

			#Verificar que hay disponibilidad para cada producto solicitado
			for row in data['items']:
				cod = row['Codigo'].strip()
				cnt = int(row['Cantidad'])

				prod = Producto.objects.get(codigo=cod)
				disp = Existencia.objects.get(producto=prod)
				if cnt > disp.cantidad:
					raise Exception('El producto '+ prod.descripcion + ' no tiene disponibilidad para ' + str(cnt) + ' Solo hay '+ str(disp.cantidad) + '.')
			#****************************************************************

			next_apartado = 0

			if Apartado.objects.count() > 0:
				next_apartado = Apartado.objects.latest('pk').no_apartado + 1
			else:
				next_apartado = 1
			
			cliente = data['cliente']
			abono = data['abono']

			o_cliente = Cliente.objects.get(pk=cliente)

			for item in data['items']:
				codigo = item['Codigo'].strip()
				cantidad = float(item['Cantidad'])
				descuento = float(item['Descuento'])
				precio = float(item['Precio'])
				total_deuda += (cantidad * precio) - descuento

				if descuento == '':
					descuento = '0'

				apartado = Apartado()
				apartado.no_apartado = next_apartado
				apartado.cliente = o_cliente
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
				abonoCte.cliente = o_cliente
				abonoCte.abono = float(abono)
				abonoCte.ap = apartado.no_apartado
				abonoCte.save()
				total_deuda = total_deuda - float(abono)

			deudaCte = DeudaCliente()

			try:	
				deudaCte = DeudaCliente.objects.get(cliente=o_cliente)
				deudaCte.deuda += int(total_deuda)
				deudaCte.save(update_fields=['deuda'])

			except deudaCte.DoesNotExist:
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
			abonos = AbonoCliente.objects.filter(cliente=o_cliente,estatus='A')
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
			montoAbono = int(data['abono'])

			o_cliente = Cliente.objects.get(pk=cliente)

			deudaCte = DeudaCliente.objects.get(cliente=o_cliente)
			
			if montoAbono > deudaCte.deuda:
				raise Exception('El monto que intenta pagar esta por encima de la deuda.')
			else:
				deudaCte.deuda -= montoAbono
				deudaCte.save()

			abono = AbonoCliente()
			abono.cliente = o_cliente
			abono.abono = montoAbono
			abono.ap = Apartado.objects.filter(cliente=o_cliente,estatus='A').latest('no_apartado').no_apartado
			abono.save()
			mensaje = 'El abono fue realizado!'

			if (deudaCte.deuda - montoAbono) <= 0:

				#CREAR UNA FACTURA PARA PRODUCTOS PAGADOS COMPLETAMENTE
				if Factura.objects.count() > 0:
					next_factura = Factura.objects.latest('pk').no_factura + 1
				else:
					next_factura = 1
		
				factura = Factura()
				factura.no_factura = next_factura
				factura.save()

				for item in Apartado.objects.filter(cliente=o_cliente,estatus='A'):
					detalle = Detalle()
					detalle.producto = item.producto
					detalle.cantidad = item.cantidad
					detalle.descuento = item.descuento
					detalle.precio = item.precio
					detalle.factura = Factura.objects.get(no_factura=next_factura)
					detalle.save()

				AbonoCliente.objects.filter(cliente=o_cliente).update(estatus='C')
				Apartado.objects.filter(cliente=o_cliente).update(estatus='C')
				
				mensaje = 'La deuda fue saldada completamente. Fue creada la factura ' + str(next_factura)


			return HttpResponse(ii)

		except Exception as e:
			return HttpResponse(e)