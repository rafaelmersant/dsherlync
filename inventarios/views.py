from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from facturas.models import Factura, Detalle
from productos.models import Producto
from .models import Inventario, Movimiento, Existencia

from .forms import InventarioForm

from django.views.generic.edit import FormView

	
class InventarioFormView(FormView):
	template_name = 'inventario.html'
	form_class = InventarioForm
	success_url = '/inventario' 

	def form_valid(self, form):
		inventario = form.save()
		
		mov = Movimiento()
		mov.producto = inventario.producto
		mov.cantidad = inventario.cantidad
		mov.tipo_movimiento = inventario.tipo_inv
		mov.save()

		cantidad = 0

		if inventario.tipo_inv == 'S':
			cantidad = inventario.cantidad
		else:
			cantidad = inventario.cantidad * -1

		existencia = Existencia()

		try:
			existencia = Existencia.objects.get(producto=inventario.producto)
			existencia.cantidad += cantidad

		except existencia.DoesNotExist:
			existencia.cantidad = cantidad
			existencia.producto = inventario.producto
		
		existencia.save()

		return super(InventarioFormView, self).form_valid(form)