from django.conf.urls import patterns, include, url

#se importa la vista
from apps.login.views import index_login

urlpatterns = [
    url(r'^$', index_login),
]