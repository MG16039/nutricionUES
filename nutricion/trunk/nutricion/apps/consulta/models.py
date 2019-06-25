from django.db import models

    #importar modelo consula r:1..*
from apps.nutricionista.models import Nutricionista
#importar modelo dieta
from apps.dieta.models import Dieta
from apps.paciente.models import Cita 
from apps.dieta.models import Requerimiento

    #from apps.dieta.models import Dieta

    # Create your models here.
    #contiene la informacion de las consultas que llegan a la Unidad de Salud
    #contiene la informacion de las patalogias de los pacientes que llegan a la Unidad de Salud

    #Contiene las tablas
        #Examen
        #Consulta
        #Patalogia
        

    #Tabla Examen 
class Examen(models.Model):

    trigliceridos = models.IntegerField()
    colesterol = models.IntegerField()
    glucosa = models.IntegerField()
    creatinina = models.IntegerField()
    acidoUrico = models.IntegerField()

    #Tabla consulta
class Consulta(models.Model):

    expediente = models.CharField(max_length = 10, primary_key = True)  #Llave primaria de consulta
    diagnostico = models.CharField(max_length = 50)
    medico = models.CharField(max_length = 20)   
    MotivoIngreso = models.CharField(max_length = 50)

    #segunda parte
    #Embarazo
    edadgestinal = models.DecimalField(max_digits=6, decimal_places=2)
    alturaUterina = models.DecimalField(max_digits=6, decimal_places=2)
    #Prematuro
    pesoAlNacer = models.DecimalField(max_digits=6, decimal_places=2)
    alturaNacimiento = models.DecimalField(max_digits=6, decimal_places=2)
    longitudNacer = models.DecimalField(max_digits=6, decimal_places=2)
    #Otros
    pesoActual = models.DecimalField(max_digits=6, decimal_places=2)
    pesoMeta = models.DecimalField(max_digits=6, decimal_places=2)
    altura = models.DecimalField(max_digits=6, decimal_places=2)
    

     #historial nutricional
    antecedentesMed = models.CharField(max_length = 50)
    antecedentesFam = models.CharField(max_length = 50)
    apetito = models.IntegerField()
    personaSirvienta =models.CharField(max_length = 50)
    suplemento = models.CharField(max_length = 50)
    otros = models.CharField(max_length = 50)

    #creamos el atributo que sera la llave foranea

    #creamos la relacion 1..* de nutricionista-consulta
    nutricion = models.ForeignKey(Nutricionista, null = True, blank = True, on_delete = models.CASCADE)
    #relacion 1..* (Agregacion) de Dieta - consulta
    dieta = models.ForeignKey(Dieta, on_delete = models.CASCADE)
    #relacion de agregacion 1..* Examen-consulta
    examen = models.OneToOneField(Examen)
    #relacion 1..1 Cita - consulta
    cita = models.OneToOneField(Cita, on_delete = models.CASCADE)
    #relacion 1..1 requerimientos - cita
    requerimieet = models.OneToOneField(Requerimiento, on_delete = models.CASCADE, blank = True)

    #tabla Patalogia
class Patalogia(models.Model):

    diagnostico = models.CharField(max_length = 15)
    tipo = models.CharField(max_length = 10)

    #creamos la relacion 1..* de consulta-Patalogia
    contiene = models.ForeignKey(Consulta, on_delete = models.CASCADE,  blank = True)

    