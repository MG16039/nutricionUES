from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#vista inicial de primera parte de registro de paciente

def index_AB(request):
    #Registro A: Datos Generales
    return render(request, 'nutricion/registroPaciente.html')


def index_CD(request):
    #Registro C: Datos Antropometricos e historial
    return render(request, 'nutricion/registroPaciente2.html')

def index_E(request):
    #Registro C: Datos Antropometricos e historial
    return render(request, 'nutricion/registroPaciente3.html')

def index_F(request):
    #Registro C: Datos Antropometricos e historial
    return render(request, 'nutricion/registroPaciente4.html')