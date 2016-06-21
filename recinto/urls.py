from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^listar/(?P<pk>[0-9]+)/$', views.listar_recintos,name="listar_recintos"),
]


