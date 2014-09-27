from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns

from productos.views import ProductoListView
from grupos.views import GrupoListView

urlpatterns = patterns('',
    # Examples:

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'facturas.views.index', name='Facturas'),

    url(r'^facturas/', 'facturas.views.index', name='Facturas'),

    url(r'^grappelli', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #API
    url(r'^api/productos/$', ProductoListView.as_view()),
    url(r'^api/grupos/$', GrupoListView.as_view()),
    url(r'^api/productos/(?P<descrp>\w+)/$', ProductoListView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)