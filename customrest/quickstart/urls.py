from django.conf.urls import url
from quickstart import views

urlpatterns = [
    url(r'^quickstart/$', views.product_list),
    url(r'^quickstart/(?P<pk>[0-9]+)/$', views.product_detail),
]
