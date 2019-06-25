from django.db import models

# Create your models here.

#Regitra los datos del usurio y los valida
    #Tabla Usuario

class Usuario(models.Model):

    #usa la llave primaria por defecto del framework
    usuario = models.CharField(max_length = 10)
    password = models.CharField(max_length = 10)
