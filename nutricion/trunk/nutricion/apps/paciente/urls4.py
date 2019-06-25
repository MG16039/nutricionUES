from django.conf.urls import patterns, include, url
#se importa la vista
from apps.paciente.views import index_F

urlpatterns = [
    url(r'^$', index_F),
]
