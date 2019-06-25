from django.db import models
from apps.nutricionista.models import Nutricionista

# Create your models here.

#contiene la informacion de los pacientes que llegan a la Unidad de Salud
#contiene la informacion de las citas de los pacientes que llegan a la Unidad de Salud
    #Tablas
        #citas
        #Paciente

    #tabla citas
class Cita(models.Model):
    
     fecha = models.DateField()
     fechaProx = models.DateField()   

#tabla Paciente
class Paciente(models.Model):

    nombres = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    expediente = models.CharField(max_length = 10,primary_key = True)   #llave primaria para Paciente
    edad = models.IntegerField()
    genero = models.CharField(max_length = 1)
    fechaNAc = models.DateField()
    estadocivil = models.CharField(max_length = 1)
    ocupacion = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 8)
    correo = models.CharField(max_length = 50)
    
    #relacion 1..* nutricionista-paciente
    nutricionista = models.ForeignKey(Nutricionista, on_delete = models.CASCADE,  blank = True)
    #paciente-citas
    cita = models.ForeignKey(Cita)
    
    