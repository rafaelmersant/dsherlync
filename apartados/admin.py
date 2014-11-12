from django.contrib import admin

from .models import Apartado, DeudaCliente, AbonoCliente

class ApartadoAdmin(admin.ModelAdmin):
	list_display = ['id','no_apartado','cliente','producto','cantidad','precio','fecha','fecha_vence','estatus']

class DeudaClienteAdmin(admin.ModelAdmin):
	list_display = ['id','cliente','deuda']

class AbonoClienteAdmin(admin.ModelAdmin):
	list_display = ['cliente','abono','fecha','ap','estatus']


admin.site.register(Apartado, ApartadoAdmin)
admin.site.register(DeudaCliente, DeudaClienteAdmin)
admin.site.register(AbonoCliente, AbonoClienteAdmin)