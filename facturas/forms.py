from .models import Factura
from django.forms import ModelForm

class FacturaForm(ModelForm):
	
	class Meta:
		model = Factura
		fields = ('no_factura')

class DetalleForm(ModelForm):

	class Meta:
		model = Detalle
		fields = ('producto','descuento','cantidad','precio','factura')