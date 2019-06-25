from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index_login(request):
    # return render(request, 'nutricion/base.html')

def index_login(request):
    #Registro A: Datos Generales
    return render(request, 'nutricion/login.html')

def index_home(request):
    #Registro home
    return render(request, 'nutricion/index.html')
