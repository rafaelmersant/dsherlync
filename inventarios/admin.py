from django.contrib import admin

from .models import Inventario, Movimiento, Existencia


class InventarioAdmin(admin.ModelAdmin):
	list_display = ['id','fecha_entrada','tipo_inv','producto','cantidad','descripcion_salida',]
	list_editable = ('fecha_entrada','tipo_inv','producto','cantidad','descripcion_salida')
	search_fields = ('producto',)
	list_filter = ('fecha_entrada',)

class MovimientoAdmin(admin.ModelAdmin):
	list_display = ['id','producto','cantidad','tipo_mov','fecha_movimiento']
	list_filter = ('producto','fecha_movimiento',)

class ExistenciaAdmin(admin.ModelAdmin):
	list_display = ['id','producto','cantidad',]
	list_filter = ('producto',)


admin.site.register(Inventario,InventarioAdmin)
admin.site.register(Movimiento,MovimientoAdmin)
admin.site.register(Existencia,ExistenciaAdmin)