from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# from rest_framework import routers
# from productos.views import ProductViewSet

# from rest_framework.urlpatterns import format_suffix_patterns
from productos import views


# router = routers.DefaultRouter()
# router.register(r'productos', ProductViewSet)

urlpatterns = patterns('',
    # Examples:

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', 'facturas.views.index', name='Facturas'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^facturas/', 'facturas.views.index', name='Facturas'),

    url(r'^grappelli', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^api/', include(router.urls)),

    #API
    url(r'^api/productos/$', 'productos.views.productos_view',),
    url(r'^api/grupos/$', 'grupos.views.grupos_view',),
    url(r'^api/productos/(?P<descrp>\w+)/$', 'productos.views.productos_view'),
)

# urlpatterns = format_suffix_patterns(urlpatterns)