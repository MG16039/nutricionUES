from django.db import models

# Create your models here.
#contiene las tablas de:
    #Alimento
    #TiempoComida
    #Dieta
    #Requerimiento

#Tabla Alimento
class Alimento(models.Model):

    nombre = models.CharField(max_length = 15)
    desc = models.DecimalField(max_digits=6, decimal_places=2)
    kcal = models.DecimalField(max_digits=6, decimal_places=2)
    lipidos = models.DecimalField(max_digits=6, decimal_places=2)
    carbohidratos = models.DecimalField(max_digits=6, decimal_places=2)
    proteinas = models.DecimalField(max_digits=6, decimal_places=2)

#Tabla Tiempo de comida
class TiempoComida(models.Model):

    tipo = models.CharField(max_length = 10)
    notas = models.CharField(max_length = 100)
    alimentos = models.ForeignKey(Alimento, on_delete = models.CASCADE,  blank = True)

#Tabla Dieta
class Dieta(models.Model):
    
    notas = models.CharField(max_length = 100)
    tiempos = models.ForeignKey(TiempoComida, on_delete = models.CASCADE,  blank = True)

class Requerimiento(models.Model):

    kcalorias = models.DecimalField(max_digits=6, decimal_places=2)
    lipidos = models.DecimalField(max_digits=6, decimal_places=2)
    carbohidratos = models.DecimalField(max_digits=6, decimal_places=2)
    proteinas = models.DecimalField(max_digits=6, decimal_places=2)