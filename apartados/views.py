from django.shortcuts import render, render_to_response

from django.views.generic.edit import FormView
from .forms import ClienteForm
from clientes.models import Cliente

class ClienteFormView(FormView):
	template_name = "apartados.html"
	form_class = ClienteForm
	success_url = '/apartados'

	def form_valid(self, form):
		cte = form.save()

		return super(ClienteFormView, self).form_valid(form)

	def post(self, request, *args, **kwargs):
		try:

			# data = json.loads(request.body)
			# items = request.body

			# next_factura = Factura.objects.latest('pk').no_factura + 1
			
			# factura = Factura()
			# factura.no_factura = next_factura
			# factura.save()
			
			# for item in data['items']:
			# 	codigo = item['Codigo'].strip()
			# 	cantidad = item['Cantidad']
			# 	descuento = float(item['Descuento'])
			# 	precio = item['Precio']

			# 	if descuento == '':
			# 		descuento = '0'

			# 	detalle = Detalle()
			# 	detalle.producto = Producto.objects.get(codigo=codigo)
			# 	detalle.cantidad = cantidad
			# 	detalle.descuento = descuento
			# 	detalle.precio = precio
			# 	detalle.factura = Factura.objects.get(no_factura=next_factura)
			# 	detalle.save()

			return HttpResponse(request.body)
			# return HttpResponse(next_factura)

		except Exception as e:
			return HttpResponse(e)

