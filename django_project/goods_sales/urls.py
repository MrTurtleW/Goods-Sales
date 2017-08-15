from django.conf.urls import patterns, include, url

import goods_sales

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^django_project/', include('django_project.foo.urls')),
    
    url(r'^$', 'goods_sales.views.index'),
    url(r'^', 'goods_sales.views.page_not_found'),
)
