from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^poke/(?P<id>\d+)$', views.pokey)
]
