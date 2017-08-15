from django.conf.urls import patterns, include, url

from goods_sales import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

from goods_sales.api.resource import MyModelResource, SalesResource, PricesResource, ChartResource

v1_api = Api(api_name='v1')
v1_api.register(MyModelResource())
v1_api.register(SalesResource())
v1_api.register(PricesResource())
v1_api.register(ChartResource())

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^django_project/', include('django_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^', include(urls)),
)
