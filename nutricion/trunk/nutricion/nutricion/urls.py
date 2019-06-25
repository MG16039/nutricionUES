from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
#from _future_ import absolut_import
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nutricion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #admin django
    url(r'^login/', include('apps.login.urls', namespace="login")), #login url y valida los datos
    #url(r'^login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^registroAB/', include('apps.paciente.urls', namespace="registroPacienteAB")), #paciente url
    url(r'^registroCD/', include('apps.paciente.urls2', namespace="registroPacienteCD")), #paciente url
    url(r'^registroE/', include('apps.paciente.urls3', namespace="registroPacienteE")), #paciente url
    url(r'^registroF/', include('apps.paciente.urls4', namespace="registroPacienteF")), #paciente url
    url(r'^home/', include('apps.login.urls2', namespace="home")), #paciente url


)
