from django.contrib import admin

from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
	list_display = ['pk', 'nombre', 'telefono']

admin.site.register(Cliente,ClienteAdmin)