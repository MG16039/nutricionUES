from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
#from _future_ import absolut_import
#admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'nutricion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #admin django

    # ---------------PARA LOGEARSE-----------------------------#
   # url(r'^login/', include('apps.login.urls', namespace="login")), #login url y valida los datos
    url(r'^$', login, {'template_name': 'nutricion/login.html'}, name = 'login'),
    #me redirige al index
    url(r'^home/$', include('apps.login.urls2', namespace= 'index_home')), #paciente url
    #Cierra sesion
    url(r'^$', logout, {'template_name': 'nutricion/login.htlm'}, name='logout' ),



    url(r'^registroAB/', include('apps.paciente.urls', namespace="registroPacienteAB")), #paciente url
    url(r'^registroCD/', include('apps.paciente.urls2', namespace="registroPacienteCD")), #paciente url
    url(r'^registroE/', include('apps.paciente.urls3', namespace="registroPacienteE")), #paciente url
    url(r'^registroF/', include('apps.paciente.urls4', namespace="registroPacienteF")), #paciente url
  #  url(r'^home/', include('apps.login.urls2', namespace="home")), #paciente url


]
