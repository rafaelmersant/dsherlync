from django.shortcuts import render
from django.http import Http404

from .models import Factura, Detalle

def  index(request):
    return render(request, 'regfactura.html')

def AgregarFactura(request, id_factura):
	if id_factura == 0:
		fact = Factura.objects.get(pk=id_factura)
	else:
		fact = Factura.save()

	
# class AgregarFactura(request):

# 	def get(self, request, descrp=None, format=None):
# 		if descrp != None:
# 			productos = Producto.objects.filter(descripcion__contains=descrp)	
# 		else:
# 			productos = Producto.objects.all()

# 		response = self.serialized_producto(productos,many=True)
# 		return Response(response.data)