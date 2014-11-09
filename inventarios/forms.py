from django import forms

from .models import Inventario, Movimiento, Existencia


class InventarioForm(forms.ModelForm):

	class Meta:
		model = Inventario
