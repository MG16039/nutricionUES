from django.conf.urls import patterns, include, url

#se importa la vista
from apps.login.views import index_home

urlpatterns = [
    url(r'^$', index_home),
]