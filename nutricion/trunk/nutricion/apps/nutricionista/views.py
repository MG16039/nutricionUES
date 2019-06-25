from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#vista inicial de login

def index_login(request):
    #Registro A: Datos Generales
    return render(request, 'nutricion/login.html')