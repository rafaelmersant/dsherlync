from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns

from productos.views import ProductoListView, ProductoDisponibleView
from clientes.views import ClienteListView
from grupos.views import GrupoListView
from facturas.views import FacturarView, FacturasDelDia, BuscarFactura, Reportes
from apartados.views import ClienteFormView, ApartarView

from inventarios.views import InventarioFormView

urlpatterns = patterns('',
    # Examples:

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'facturas.views.index', name='Facturas'),
    url(r'^facturas/$', 'facturas.views.index', name='Facturas'),

    #REPORTES
    url(r'^reportes/$', Reportes.as_view(), name='Reportes'),
    url(r'^buscarfactura/$', BuscarFactura.as_view(), name='Buscar Facturas'),

    url(r'^inventario/$', InventarioFormView.as_view(), name='Inventario'),    

    url(r'^facturasdeldia/$', FacturasDelDia.as_view(), name='Facturas'),
    url(r'^facturasdeldia/(?P<Fecha>[\w\-]+)/$', FacturasDelDia.as_view(), name='Facturas'),
    url(r'^facturar/$', FacturarView.as_view(), name='Facturar'),
    url(r'^apartados/$', ClienteFormView.as_view(), name='Cliente'),
    url(r'^apartar/$', ApartarView.as_view(), name='Apartados'),

    url(r'^grappelli', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #API
    url(r'^api/proddisp/(?P<Prod>[\w]+)/$', ProductoDisponibleView.as_view()),
   
    url(r'^api/productos/$', ProductoListView.as_view()),
    url(r'^api/productos/(?P<descrp>[\w\s]+)/$', ProductoListView.as_view()),
    
    url(r'^api/clientes/$', ClienteListView.as_view()),
    url(r'^api/clientes/(?P<nombre>[\w\s]+)/$', ClienteListView.as_view()),

    url(r'^api/grupos/$', GrupoListView.as_view()),
    url(r'^api/grupos/(?P<pk>\w+)/$', GrupoListView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)